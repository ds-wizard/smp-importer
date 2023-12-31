class MappingExecutor:

    def __init__(self):
        self.result = []

    def result_add(self, action: str, **kwargs):
        self.result.append({
            'type': action,
            **kwargs,
        })

    def result_debug(self, message: str):
        self.result_add(action='debug', message=message)

    def result_add_item(self, path: str, var_name: str):
        self.result_add(action='addItem', path=path.split('.'), var=var_name)

    def result_set_reply(self, path: str, value: str):
        self.result_add(action='setReply', path=path.split('.'), value=value)

    def result_set_integration_reply(self, path: str, value: str, item_id):
        self.result_add(action='setIntegrationReply', path=path.split('.'), value=value, itemId=item_id)

    def get_result_dict(self):
        return {
            'actions': self.result,
        }
