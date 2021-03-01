from ipywidgets import HBox, VBox, Button, Layout, FloatProgress, Output
import hublib.ui as ui
import random, string
from string import Template
from secrets import SECRETS
from scgi_utils import TemplatePW

from ipywidgets import Password
from  hublib.ui.formvalue import FormValue
class MyPassword(FormValue):
    def __init__(self, name, value, **kwargs):
        self.dd = Password(value=value)
        FormValue.__init__(self, name, **kwargs)
        

def GetInputFile():
    in_input_file = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return in_input_file

##################################################
# Conection
##################################################

SCGI_UI = {}
SCGI_UI['s0'] = {}
SCGI_UI['s0']['pwd'] = MyPassword('SCGI Password',SECRETS['PWD'])
SCGI_UI['s0']['code'] = MyPassword('Dual AUTH Code',SECRETS['CODE'])
SCGI_UI['s0']['user'] = ui.String('SCGI User name',SECRETS['USER'])
SCGI_UI['s0']['folder'] = ui.String('Working folder',SECRETS['ID'] + "/" + SECRETS['USER'] + "/" + GetInputFile())
SCGI_UI['s0']['button'] = Button(description='Connect')
SCGI_UI['s0']['status'] = ui.String('Status','')
SCGI_UI['s0']['status'].dd.layout = Layout(width='100%')
SCGI_UI['s0']['status'].disabled = True
SCGI_UI['s0']['display'] = ui.Form([
            SCGI_UI['s0']['user'], 
            SCGI_UI['s0']['pwd'], 
            SCGI_UI['s0']['code'], 
            SCGI_UI['s0']['folder'], 
            HBox([SCGI_UI['s0']['button']]),
            SCGI_UI['s0']['status'],            
        ], name = 'Credentials')


SCGI_UI['s_0'] = {}
SCGI_UI['s_0']['pwd1'] = MyPassword('TACC Password',SECRETS['PWD'])
SCGI_UI['s_0']['pwd2'] = MyPassword('PURDUE Password',SECRETS['PWD'])
SCGI_UI['s_0']['code'] = MyPassword('TACC AUTH Code',SECRETS['CODE'])
SCGI_UI['s_0']['user1'] = ui.String('TACC User name',SECRETS['USER'])
SCGI_UI['s_0']['user2'] = ui.String('PURDUE User name',SECRETS['USER'])
SCGI_UI['s_0']['folder1'] = ui.String('TACC Working folder',SECRETS['ID'] + "/" + SECRETS['USER'] + "/" + GetInputFile())
SCGI_UI['s_0']['folder2'] = ui.String('PURDUE Working folder',SECRETS['ID'] + "/" + SECRETS['USER'] + "/" + GetInputFile())
SCGI_UI['s_0']['button'] = Button(description='Connect')
SCGI_UI['s_0']['status'] = ui.String('Status','')
SCGI_UI['s_0']['status'].dd.layout = Layout(width='100%')
SCGI_UI['s_0']['status'].disabled = True
SCGI_UI['s_0']['display'] = ui.Form([
            SCGI_UI['s_0']['user1'], 
            SCGI_UI['s_0']['pwd1'], 
            SCGI_UI['s_0']['folder1'], 
            SCGI_UI['s_0']['code'], 
            SCGI_UI['s_0']['user2'], 
            SCGI_UI['s_0']['pwd2'], 
            SCGI_UI['s_0']['folder2'], 
            HBox([SCGI_UI['s_0']['button']]),
            SCGI_UI['s_0']['status'],            
        ], name = 'Credentials')

##################################################
# First
##################################################

SCGI_UI['s1'] = {}
SCGI_UI['s1']['ecutwfc'] = ui.String('ecutwfc','40.0')
SCGI_UI['s1']['kpoints'] = ui.Text(
    name="kpoints",
    value='''automatic
6 6 6 1 1 1'''    
)
SCGI_UI['s1']['kpoints'].dd.layout = Layout(height='120px')
SCGI_UI['s1']['input'] = ui.Text( name="inputdeck", value='''''')
SCGI_UI['s1']['input'].dd.layout = Layout(width='90%', height='150px')
SCGI_UI['s1']['input'].disabled = True

SCGI_UI['s1']['commands'] = ui.Text( name="commands", value='''''')
SCGI_UI['s1']['commands'].dd.layout = Layout(width='90%', height='150px')
SCGI_UI['s1']['commands'].disabled = True

SCGI_UI['s1']['stdin'] = ui.Text( name="stdin", value='''''')
SCGI_UI['s1']['stdin'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s1']['stdin'].disabled = True

SCGI_UI['s1']['stdout'] = ui.Text( name="stdout", value='''''')
SCGI_UI['s1']['stdout'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s1']['stdout'].disabled = True

SCGI_UI['s1']['stderr'] = ui.Text( name="stderr", value='''''')
SCGI_UI['s1']['stderr'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s1']['stderr'].disabled = True

SCGI_UI['s1']['button'] = Button(description='Calculate Self Consistency')
SCGI_UI['s1']['button'].layout = Layout(width='99%')
SCGI_UI['s1']['job_id'] = ui.String('job ID','')
SCGI_UI['s1']['job_id'].disabled = True
SCGI_UI['s1']['status'] = ui.String('job status','')
SCGI_UI['s1']['status'].disabled = True
SCGI_UI['s1']['button_status'] = Button(description='Update Status')
SCGI_UI['s1']['button_status'].layout = Layout(width='99%')

SCGI_UI['s1']['l1'] = VBox([
                               SCGI_UI['s1']['ecutwfc'],
                               SCGI_UI['s1']['kpoints'],
                               SCGI_UI['s1']['button'],
                               SCGI_UI['s1']['job_id'],
                               SCGI_UI['s1']['status'],                               
                              ])
SCGI_UI['s1']['l2'] = VBox([
                               SCGI_UI['s1']['input'],
                               SCGI_UI['s1']['commands'],                               
                              ])
SCGI_UI['s1']['bs'] = HBox([SCGI_UI['s1']['l1'],SCGI_UI['s1']['l2']])
SCGI_UI['s1']['l2'].layout = Layout(width='100%', border='1px')
SCGI_UI['s1']['bs'].layout = Layout(width='100%', border='1px')

s1_tab0 = ui.Form([SCGI_UI['s1']['bs']], name = 'Crystal Inputs')
s1_tab1 = ui.Form([SCGI_UI['s1']['stdin']], name = 'stdin')
s1_tab2 = ui.Form([SCGI_UI['s1']['stdout']], name = 'stdout')
s1_tab3 = ui.Form([SCGI_UI['s1']['stderr']], name = 'stderr')


def UpdateStep1( event ):
    global SCGI_UI, SCGI
    change = {  'k_points':SCGI_UI['s1']['kpoints'].value, 
                'prefix':'gaas',
                'calculation':'scf',
                'crystal':'crystal',
                'system_params':'ecutwfc = ' + SCGI_UI['s1']['ecutwfc'].value + "," }

    if event['type'] == 'change' and event['name'] == 'value' and event['new']:
        SCGI_UI['s1']['input'].value = TemplatePW().safe_substitute(change)
    
SCGI_UI['s1']['ecutwfc'].dd.observe(UpdateStep1)
SCGI_UI['s1']['kpoints'].dd.observe(UpdateStep1)
SCGI_UI['s1']['display'] = ui.Tab([s1_tab0, s1_tab1, s1_tab2, s1_tab3])
UpdateStep1({'type':'change','name':'value','new':'new'})


##################################################
# Second
##################################################

SCGI_UI['s2'] = {}

SCGI_UI['s2']['nbnd'] = ui.String('nbnd','8')
SCGI_UI['s2']['ecutwfc'] = ui.String('ecutwfc','40.0')
SCGI_UI['s2']['kpoints'] = ui.Text(
    name="kpoints",
    value='''tpiba_b
3
0.500 0.500 0.500 20
0.000 0.000 0.000 20
1.000 0.000 0.000 20'''    
)
SCGI_UI['s2']['kpoints'].dd.layout = Layout(height='120px')
SCGI_UI['s2']['input'] = ui.Text( name="inputdeck", value='''''')
SCGI_UI['s2']['input'].dd.layout = Layout(width='90%', height='150px')
SCGI_UI['s2']['input'].disabled = True

SCGI_UI['s2']['commands'] = ui.Text( name="commands", value='''''')
SCGI_UI['s2']['commands'].dd.layout = Layout(width='90%', height='150px')
SCGI_UI['s2']['commands'].disabled = True

SCGI_UI['s2']['stdin'] = ui.Text( name="stdin", value='''''')
SCGI_UI['s2']['stdin'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s2']['stdin'].disabled = True

SCGI_UI['s2']['stdout'] = ui.Text( name="stdout", value='''''')
SCGI_UI['s2']['stdout'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s2']['stdout'].disabled = True

SCGI_UI['s2']['stderr'] = ui.Text( name="stderr", value='''''')
SCGI_UI['s2']['stderr'].dd.layout = Layout(width='100%', height='300px')
SCGI_UI['s2']['stderr'].disabled = True

SCGI_UI['s2']['button'] = Button(description='Calculate BandStructure')
SCGI_UI['s2']['button'].layout = Layout(width='99%')
SCGI_UI['s2']['job_id'] = ui.String('job ID','')
SCGI_UI['s2']['job_id'].disabled = True
SCGI_UI['s2']['status'] = ui.String('job status','')
SCGI_UI['s2']['status'].disabled = True

SCGI_UI['s2']['l1'] = VBox([
                               SCGI_UI['s2']['nbnd'],
                               SCGI_UI['s2']['ecutwfc'],
                               SCGI_UI['s2']['kpoints'],
                               SCGI_UI['s2']['button'],
                               SCGI_UI['s2']['job_id'],
                               SCGI_UI['s2']['status'],                               
                              ])
SCGI_UI['s2']['l2'] = VBox([
                               SCGI_UI['s2']['input'],
                               SCGI_UI['s2']['commands'],                               
                              ])
SCGI_UI['s2']['bs'] = HBox([SCGI_UI['s2']['l1'],SCGI_UI['s2']['l2']])
SCGI_UI['s2']['l2'].layout = Layout(width='100%', border='1px')
SCGI_UI['s2']['bs'].layout = Layout(width='100%', border='1px')

s2_tab0 = ui.Form([SCGI_UI['s2']['bs']], name = 'band-structure Inputs')
s2_tab1 = ui.Form([SCGI_UI['s2']['stdin']], name = 'stdin')
s2_tab2 = ui.Form([SCGI_UI['s2']['stdout']], name = 'stdout')
s2_tab3 = ui.Form([SCGI_UI['s2']['stderr']], name = 'stderr')


def UpdateStep2( event ):
    global SCGI_UI, SCGI
    change = {  'k_points':SCGI_UI['s2']['kpoints'].value, 
                'prefix':'gaas',
                'calculation':'bands',
                'crystal':'',
                'system_params':'ecutwfc = ' + SCGI_UI['s2']['ecutwfc'].value + ',\nnbnd = ' + SCGI_UI['s2']['nbnd'].value + ',' }

    if event['type'] == 'change' and event['name'] == 'value' and event['new']:
        SCGI_UI['s2']['input'].value = TemplatePW().safe_substitute(change)

SCGI_UI['s2']['nbnd'].dd.observe(UpdateStep2)
SCGI_UI['s2']['kpoints'].dd.observe(UpdateStep2)
UpdateStep2({'type':'change','name':'value','new':'new'})
SCGI_UI['s2']['display'] = ui.Tab([s2_tab0, s2_tab1, s2_tab2, s2_tab3])


##################################################
# Third
##################################################

SCGI_UI['s3'] = {}
SCGI_UI['s3']['button'] = Button(description='Extract BandStructure')
SCGI_UI['s3']['button'].layout = Layout(width='99%')

SCGI_UI['s3']['input'] = ui.Text( name="inputs", value='''''')
SCGI_UI['s3']['input'].dd.layout = Layout(width='100%', height='470px')
SCGI_UI['s3']['input'].disabled = True

SCGI_UI['s3']['output'] = Output()
SCGI_UI['s3']['output'].layout = Layout(width='99%')

SCGI_UI['s3']['l1'] = VBox([
                               SCGI_UI['s3']['input'],
                               SCGI_UI['s3']['button'],
                              ])
SCGI_UI['s3']['l2'] = VBox([
                               SCGI_UI['s3']['output'],
                              ])
SCGI_UI['s3']['bs'] = HBox([SCGI_UI['s3']['l1'],SCGI_UI['s3']['l2']])
SCGI_UI['s3']['l1'].layout = Layout(width='50%', border='1px')
SCGI_UI['s3']['l2'].layout = Layout(width='50%', border='1px')
SCGI_UI['s3']['bs'].layout = Layout(width='100%', border='1px')

SCGI_UI['s3']['display'] = ui.Form([SCGI_UI['s3']['bs']], name = 'band-structure Visualization')
