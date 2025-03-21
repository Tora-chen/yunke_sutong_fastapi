# 这个文件的作用是将所有的实体类导入，
# 这样在其他地方导入entity包时，就可以直接导入entity包，而不需要导入entity下的每个实体类

from .User import User
from .Lecture import Lecture
from .Video import Video
from .Note import Note
from .Role import Role
from .UserRole import UserRole
from .UserCollection import UserCollection
from .Caption import Caption
