import mock
from nose.tools import assert_equals
from nose.tools import assert_not_equal
from library import pylxca_module


# this dict is used to get command_options
func_dict = {
                'connect': pylxca_module._get_connect_lxca,
                'chassis': pylxca_module._get_chassis_inventory,
                'cmms': pylxca_module._get_cmms_inventory,
                'get_configpatterns': pylxca_module._get_configpatterns,
                'get_particular_configpattern': pylxca_module._get_particular_configpattern,
                'import_configpatterns': pylxca_module._import_configpatterns,
                'apply_configpatterns': pylxca_module._apply_configpatterns,
                'configprofiles': pylxca_module._get_configprofiles,
                'configtargets': pylxca_module._get_configtargets,
                'get_configstatus': pylxca_module._get_configstatus,
                'discover': pylxca_module._get_discover,
                'fans': pylxca_module._get_fans,
                'fanmuxes': pylxca_module._get_fanmuxes,
                'ffdc': pylxca_module._get_ffdc,
                'jobs': pylxca_module._get_jobs,
                'lxcalog': pylxca_module._get_lxcalog,
                'manage': pylxca_module._manage_endpoint,
                'unmanage': pylxca_module._unmanage_endpoint,
                'manage_status': pylxca_module._manage_status,
                'unmanage_status': pylxca_module._unmanage_status,
                'nodes': pylxca_module._get_nodes,
                'osimages': pylxca_module._get_osimages,
                'powersupplies': pylxca_module._get_powersupplies,
                'scalablesystem': pylxca_module._get_scalablesystem,
                'switches': pylxca_module._get_switches_inventory,
                'tasks': pylxca_module._get_tasks,
                'updaterepo': pylxca_module._get_updaterepo_info,
                'update_firmware': pylxca_module._update_firmware,
                'update_firmware_all': pylxca_module._update_firmware_all,
                'update_firmware_query_status':pylxca_module._update_firmware_query_status,
                'update_firmware_query_comp':pylxca_module._update_firmware_query_comp,
                'get_managementserver_pkg': pylxca_module._get_managementserver_pkg,
                'update_managementserver_pkg': pylxca_module._update_managementserver_pkg,
                'import_managementserver_pkg': pylxca_module._import_managementserver_pkg,
                'updatepolicy': pylxca_module._get_updatepolicy,
                'users': pylxca_module._get_users,

}

expected_arguments_spec = dict(
    login_user=dict(default=None, required=False),
    login_password=dict(default=None, required=False),
    connobject=dict(default=None),
    command_options=dict(choises=list(func_dict)),
    lxca_action=dict(default=None),
    auth_url=dict(default=None),
    uuid=dict(default=None),
    id=dict(default=None),
    endpoint_ip=dict(default=None),
    jobid=dict(default=None),
    user=dict(default=None, required=False),
    password=dict(default=None, required=False),
    force=dict(default=None),
    percentage=dict(default=None),
    state=dict(default=None),
    sol_id=dict(default=None),
    description=dict(default=None),
    solutionVPD=dict(default=None, type=('dict')),
    members=dict(default=None, type=('list')),
    criteria=dict(default=None, type=('list')),
    recovery_password=dict(default=None),
    repo_key=dict(default=None),
    mode=dict(default=None),
    server=dict(default=None),
    storage=dict(default=None),
    switch=dict(default=None),
    cmm=dict(default=None),
    policy_info=dict(default=None),
    policy_name=dict(default=None),
    policy_type=dict(default=None),
    update_list=dict(default=None, type=('list')),
    fact_dict=dict(default=None, type=('dict')),
    machine_type=dict(default=None),
    fixids=dict(default=None),
    scope=dict(default=None),
    file_type=dict(default=None),
    endpoint=dict(default=None),
    restart=dict(default=None),
    type=dict(default=None),
    config_pattern_name=dict(default=None),
    config_profile_name=dict(default=None),
    resource_group_name=dict(default=None),
    delete_profile=dict(default=None),
    unassign=dict(default=None),
    powerdown=dict(default=None),
    resetimm=dict(default=None),
    pattern_update_dict=dict(default=None, type=('dict')),
    includeSettings=dict(default=None),
    osimages_info=dict(default=None),
    osimages_dict=dict(default=None, type=('dict')),
    update_key=dict(default=None),
    files=dict(default=None),
    unittest=dict(default=None),
    uuid_list=dict(default=None, type=('list')),
    storedcredential_id=dict(default=None)
)


class TestPylxcaMod:
    '''
    this test shows how to mock AnsibleModule and set args for return value
    it calls nodes to gett actual nodes from LXCA
    '''

    @mock.patch("library.pylxca_module.AnsibleModule", autospec=True)
    def test__main__success(self, ansible_mod_cls):
        mod_obj = ansible_mod_cls.return_value
        args = {
                "auth_url": "https://10.243.12.139",
                 "login_user": "USERID",
                 "login_password": "CME44ibm",
                 "command_options": "connect",
                 "unittest": None,
               }
        mod_obj.params = args 
        connection_obj = pylxca_module.main()
        print(" Return from main")
        print connection_obj

        assert_equals(mock.call(argument_spec=expected_arguments_spec,
                                check_invalid_arguments=False,supports_check_mode = False), ansible_mod_cls.call_args)

        #assert_not_equal(connection_obj.exit_json.result, [])
    '''
    This test mocks AnsibleModule and _get_nodes also
    call to pylxca_module.main will not fetch data from LXCA
    '''
    @mock.patch("library.pylxca_module._get_nodes", autospec=True)
    @mock.patch("library.pylxca_module.AnsibleModule", autospec=True)
    def test__main_nodes(self, ansible_mod_cls,_get_nodes):
        mod_obj = ansible_mod_cls.return_value
        args = {
                "auth_url": "https://10.243.12.139",
                 "login_user": "USERID",
                 "login_password": "CME44ibm",
                 "command_options": "nodes",
                 "unittest": "True",
               }
        mod_obj.params = args
        #pylxca_module.main()

        empty_nodes_list = []
        _get_nodes.return_value = empty_nodes_list
        ret_nodes = pylxca_module.main()
        print("main nodes output ")
        print ret_nodes
    	#assert(mock.call(argument_spec=expected_arguments_spec) != ansible_mod_cls.call_args)
        assert_equals(mock.call(argument_spec=expected_arguments_spec,
                                check_invalid_arguments=False, supports_check_mode=False), ansible_mod_cls.call_args)
        assert_not_equal(mock.call(mod_obj, mod_obj.params),_get_nodes.call_args)
        #assert(_get_nodes.return_value, ret_nodes)


    '''
    This test mocks AnsibleModule and _get_nodes also
    call to _get_nodes will not fetch data from LXCA
    '''
    @mock.patch("library.pylxca_module._get_nodes", autospec=True)
    @mock.patch("library.pylxca_module.AnsibleModule", autospec=True)
    def test__nodes(self, ansible_mod_cls,_get_nodes):
        mod_obj = ansible_mod_cls.return_value
        args = {
                "auth_url": "https://10.243.12.139",
                 "login_user": "USERID",
                 "login_password": "CME44ibm",
                 "command_options": "nodes",
               }
        mod_obj.params = args
        #pylxca_module.main()
        expected_arguments_spec=dict(
            login_user      = dict(default=None, required=False),
            login_password  = dict(default=None, required=False),
            connobject      = dict(default=None),
            command_options = dict( choises=list(func_dict) ),
            action          = dict(default=None),
            auth_url        = dict(default=None),
            uuid            = dict(default=None),
            )

        empty_nodes_list = []
        _get_nodes.return_value = empty_nodes_list
        ret_nodes = _get_nodes(mod_obj, args)
        print("nodes output ")
        print ret_nodes
    	#assert(mock.call(argument_spec=expected_arguments_spec) != ansible_mod_cls.call_args)
        # Assert call to _get_connect_lxca
        assert(mock.call(mod_obj, mod_obj.params) == _get_nodes.call_args)
        assert_equals(_get_nodes.return_value, ret_nodes)
