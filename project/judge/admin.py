from django.contrib import admin

# register your models here.

from .models import ParentScoreCategory
from .models import ScoreCategory
from .models import ScoreMetric
from .models import Gender
from .models import Level
from .models import Division
from .models import Category
from .models import Team
from .models import Round
from .models import Championship
from .models import Registration
from .models import ScoreSheet
from .models import UserScoreSheetElement
from .models import ScoreSheetType
from .models import ScoreSheetElement
from .models import UserSkillPermission

admin.site.register(ParentScoreCategory)
admin.site.register(ScoreCategory)
admin.site.register(ScoreMetric)
admin.site.register(Gender)
admin.site.register(Level)
admin.site.register(Division)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Round)
admin.site.register(Championship)
admin.site.register(Registration)
admin.site.register(ScoreSheet)
admin.site.register(UserScoreSheetElement)
admin.site.register(ScoreSheetType)
admin.site.register(ScoreSheetElement)
admin.site.register(UserSkillPermission)