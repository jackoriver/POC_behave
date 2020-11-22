from TestlinkApiClient.tlxmlrpc import TestlinkClient


def connect_to_testlink(context):
    context.testlink = TestlinkClient(url=context.config.userdata.get('testlink_url'), user=context.config.userdata.get('testlink_user'),
                                      dev_key=context.config.userdata.get('testlink_dev_key'))


def update_tc_result(context, tc_id, result):
    context.testlink.set_execution_result(project_name=context.project_name, plan_name=context.plan_name, platform_name=context.platform_name,
                                              build_name=context.build_name, case_ext_id=tc_id, case_exe_result=result)
