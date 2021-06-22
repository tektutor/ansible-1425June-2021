#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def printMsg(msg1,msg2):
    return msg1 + " " + msg2

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg1=dict(type='str'),
            msg2=dict(type='str'),
        )
    )   

    mesg1=module.params['msg1']
    mesg2=module.params['msg2']
    output = printMsg( mesg1, mesg2 )

    result = dict(
       msg=output
    )   

    module.exit_json(**result, changed=False)
    #module.fail_json(msg="Error occured")


if __name__ == '__main__':
    main()
