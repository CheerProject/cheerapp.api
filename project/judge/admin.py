from django.contrib import admin

# register your models here.

from .models import ParentScoreCategory
from .models import ScoreCategory
from .models import ScoreMetric
from .models import Level
from .models import Team
from .models import Round
from .models import Championship
from .models import Registration
from .models import UserScoreCategoryChampionship
from .models import ScoreSheet

admin.site.register(ParentScoreCategory)
admin.site.register(ScoreCategory)
admin.site.register(ScoreMetric)
admin.site.register(Level)
admin.site.register(Team)
admin.site.register(Round)
admin.site.register(Championship)
admin.site.register(Registration)
admin.site.register(UserScoreCategoryChampionship)
admin.site.register(ScoreSheet)