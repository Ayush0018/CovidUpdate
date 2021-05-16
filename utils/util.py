from configparser import ConfigParser


class Utilities:

    @staticmethod
    def read_config(section, param):
        config = ConfigParser()
        config.read(r"../Config/config.ini")
        return config.get(section, param)

        # if isinstance(var_type, str):
        #     return config.get(section, param)
        #
        # elif isinstance(var_type, bool):
        #     return config.getboolean(section, param)
        #
        # elif isinstance(var_type, int):
        #     return config.getint(section, param)
        #
        # elif isinstance(var_type, float):
        #     return config.getint(section, param)
