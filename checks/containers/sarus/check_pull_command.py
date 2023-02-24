import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class SarusPullCommandCheck(rfm.RunOnlyRegressionTest):
    sourcesdir = None
    valid_systems = ['dom:gpu', 'dom:mc', 'daint:gpu', 'daint:mc',
                     'eiger:mc', 'pilatus:mc', 'hohgant:nvgpu', 'hohgant:cpu']
    valid_prog_environs = ['builtin']
    num_tasks = 1
    num_tasks_per_node = 1
    executable = 'sarus pull alpine && echo CHECK_SUCCESSFUL'
    prerun_cmds = ['sarus --version', 'unset XDG_RUNTIME_DIR']
    maintainers = ['amadonna', 'taliaga']
    tags = {'production'}

    @run_after('setup')
    def set_modules(self):
        if self.current_system.name not in {'eiger', 'pilatus', 'hohgant'}:
            self.modules = ['sarus']

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'CHECK_SUCCESSFUL', self.stdout)
