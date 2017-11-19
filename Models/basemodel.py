class BaseModel(object):

    def __init__(self):
        pass

    def build_from_json(self,json_config):
        config_section = json_config[self.config_outname]
        for key,value in config_section.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
    