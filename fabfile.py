from fabric.api import local, task, execute
from os.path import join

# Third-party libraries
vendor = [
    'jquery/dist/jquery.js',
]

# Our source code
src = [
    'src/helper/controller.js',
    'src/helper/greeter.js',
]


@task
def setup():
    "Installs and links all the js libraries"
    local('npm install')
    local('mkdir src/vendor')
    local('cp node_modules/* src/vendor/ -r')


@task
def clean():
    local('rm -rf build/*')


@task
def compile():
    execute(clean)
    src_string = " ".join(src)
    ven_string = " ".join([join('node_modules', l) for l in vendor])
    cmd = 'node_modules/.bin/traceur --out build/main.js --modules=amd --script src/main.js {} {}'
    local(cmd.format(ven_string, src_string))
    local('cp node_modules/requirejs/require.js build/')
    local('cp node_modules/traceur/bin/traceur-runtime.js build/')


