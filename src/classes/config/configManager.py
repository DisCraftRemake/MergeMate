import yaml
import ruamel.yaml


class ConfigManager:
    def __init__(self, config: str) -> None:
        self.config = config
        pass

    def access_nested_dict(self, nested_dict, keys):
        result = nested_dict
        for key in keys:
            if isinstance(result, dict) and key in result:
                result = result[key]
            else:
                return None
        return result

    def getNamespaceAsDict(self, namespace: str) -> dict:
        with open(self.config, 'r') as config_yaml:
            config = yaml.safe_load(config_yaml)

        if namespace:
            keys = namespace.split('.')
            data = config
            for key in keys:
                if key in data:
                    data = data[key]
                else:
                    return {}
            return data
        else:
            return {}

    def replace(self, namespace: str, new_value) -> None:
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True

        with open(self.config, 'r') as configYAML:
            config = yaml.load(configYAML)

        namespace_keys = namespace.split('.')
        current = config
        for key in namespace_keys[:-1]:
            current = current.get(key, {})

        last_key = namespace_keys[-1]
        if last_key in current:
            current[last_key] = new_value

            with open(self.config, 'w') as configYAML:
                yaml.dump(config, configYAML)
        else:
            print(f"Namespace '{namespace}' not found in the configuration.")


    def get(self, object: str) -> str:
        if("." in object):
            args = object.split(".")
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)
            result = self.access_nested_dict(config, args)
            return result
        else:
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)

                return config[object]

    def getString(self, object: str) -> str:
        if("." in object):
            args = object.split(".")
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)
            result = self.access_nested_dict(config, args)
            return result
        else:
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)

                return config[object]

    def getInt(self, object: str) -> int:
        if("." in object):
            args = object.split(".")
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)
            result = self.access_nested_dict(config, args)
            return result
        else:
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)

                return config[object]

    def getBool(self, object: str) -> bool:
        if("." in object):
            args = object.split(".")
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)
            result = self.access_nested_dict(config, args)
            return result
        else:
            with open(self.config) as configYAML:
                config = yaml.safe_load(configYAML)

                return config[object]
