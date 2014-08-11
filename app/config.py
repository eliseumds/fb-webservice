from tornado.options import define,options,parse_config_file,parse_command_line

define('debug',default=True)
define('env',default='./dev.conf')
define('rest_port',default=5001)
define('db_log',default='log.db')
define('db_main',default='main.db')
define('test',default=True)
define('version',default='0.0.0')

parse_command_line()
parse_config_file(options.env)
