import jmespath
import json
from string import Template
   
def TemplatePW():
    return Template('''&control
calculation = '${calculation}'
prefix = '${prefix}',
pseudo_dir = './',
outdir = './'
/
&system
ibrav = 2,
celldm(1) = 10.4749,
nat = 2,
ntyp = 2,
${system_params}
/
&electrons
/
ATOMIC_SPECIES
Ga 1.0 Ga.pz-bhs.UPF
As 1.0 As.pz-bhs.UPF
ATOMIC_POSITIONS ${crystal}
Ga 0.00 0.00 0.00
As 0.25 0.25 0.25
K_POINTS ${k_points}''')
            
def TemplatePBS() :
    return Template('''#!/bin/bash -l
#SBATCH
#SBATCH -J $job_name
#SBATCH -o $job_name.out
#SBATCH -e $job_name.err
#SBATCH -N $nodes
#SBATCH -n $tasks
#SBATCH -p $partition 
#SBATCH -t $time
$modules
$command''')

def GetPbs( template, input_file, command='pw.x', partition='normal', mpirun='ibrun', modules='' ):
    change = {  'job_name':input_file,
                'time':'01:00:00',
                'partition':partition,
                'nodes':'1',
                'tasks':'12',
                'mem':'1000MB',
                'modules':modules,
                'command':mpirun +' -np 12 '+ command +' -input ' + input_file + '.in >' + input_file + '.out '}
    return template.safe_substitute(change)
    
def getStatus( session, code, buffer = None ):
    command = "squeue -j " + str(code) + " | tail -1"
    try :
        stdin, stdout, stderr, command = session.execute(command, buffer);
        line = stdout[len(stdout)-1].strip('\n')
        columns = line.split()
        if (len(columns) < 7):
            status = 'X'
        elif columns[0] == "JOBID":
            status = "CG"
        else :
            status = str(columns[4])
            if (status == "R"):
                command = "ls *o" + str(code)
                stdin, stdout, stderr, command = session.execute(command, buffer);
                if (len(stdout) > 0):
                    command = "scancel " + str(code)
                    stdin, stdout, stderr, command = session.execute(command, buffer);  
                    status = "CG"
    except :
        status = 'X'
        line = "ERROR"
    return status, line, command

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False