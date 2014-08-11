from .model import Log
import simplejson

__all__ = ['log']

class Logging():
    def _save(self,text,arguments=None,type='INFO'):
        Log.create(arguments=simplejson.dumps(arguments),
                   text=text,
                   type=type)
        return True

    def error(self,text,arguments=None):
        return self._save(text,arguments,type='ERROR')

    def info(self,text,arguments=None):
        return self._save(text,arguments,type='INFO')

    def warn(self,text,arguments=None):
        return self._save(text,arguments,type='WARN')

log = Logging()
