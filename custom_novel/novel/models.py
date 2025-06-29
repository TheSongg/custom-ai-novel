from django.contrib.auth.models import User
from django.db import models
from django_softdelete.models import SoftDeleteModel


class Novel(SoftDeleteModel):
    CATEGORY_CHOICES = {
        1: {"en":"Modern Romance", "zh": "都市言情"},
        2: {"en":"Science Fiction", "zh": "科幻小说"},
        3: {"en":"Mystery & Thriller", "zh": "悬疑推理"},
        4: {"en":"Historical Fiction", "zh": "历史小说"},
        5: {"en":"Wuxia & Xiuxian", "zh": "武侠与修仙"},
    }
    name = models.CharField(max_length=100, verbose_name='Novel Name/小说名称')
    category = models.CharField(max_length=100, verbose_name='Novel Category/小说分类',
                                choices=[(key, value["zh"]) for key, value in CATEGORY_CHOICES.items()])
    theme = models.CharField(max_length=300, verbose_name='Novel Theme/小说主题')
    introduction = models.CharField(max_length=1000, verbose_name='Novel Introduction/小说简介')
    remake = models.CharField(max_length=1000, verbose_name='Remake/备注')
    word_count = models.IntegerField(default=0, verbose_name='Novel Word Count/总字数')
    recommendation_num = models.IntegerField(default=0, verbose_name='Novel Recommendation Number/推荐数')
    completed = models.BooleanField(default=False, verbose_name='Novel Completed/是否完结')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created by', related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Updated by', related_name='updated_by')

    class Meta:
        db_table = 'novel'
        ordering = ['-id']


class Chapter(SoftDeleteModel):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='Novel', related_name='chapters')
    chapter_title= models.CharField(max_length=100, verbose_name='Chapter Title/本章标题')
    chapter_text = models.TextField(verbose_name='Chapter Text/本章正文')
    chapter_summary = models.TextField(max_length=300, verbose_name='Chapter Summary/本章簡述')
    chapter_word_count = models.IntegerField(default=0, verbose_name='Chapter Word Count/本章字數')
    chapter_role = models.CharField(max_length=100, verbose_name='Chapter Role/本章定位')
    chapter_purpose = models.CharField(max_length=100, verbose_name='Chapter Purpose/核心作用')
    suspense_level = models.CharField(max_length=100, verbose_name='Suspense Level/悬念密度')
    foreshadowing = models.CharField(max_length=100, verbose_name='Foreshadowing/伏笔')
    plot_twist_level = models.CharField(max_length=100, verbose_name='Plot Twist Level/认知颠覆')

    class Meta:
        db_table = 'chapter'
        ordering = ['-id']


class NovelSetting(SoftDeleteModel):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='Novel', related_name='settings')
    core_seed = models.CharField(max_length=400, verbose_name='Core Seed/核心种子')
    character_dynamics = models.CharField(max_length=5000, verbose_name='Character Dynamics/角色动力学')
    world_view = models.CharField(max_length=5000, verbose_name='World View/世界观')
    plot_architecture = models.CharField(max_length=5000, verbose_name='Plot Architecture/情节架构')
    chapter_blueprint = models.CharField(max_length=5000, verbose_name='Chapter Blueprint/章节蓝图')

    class Meta:
        db_table = 'novel_setting'
        ordering = ['-id']


class NovelRole(SoftDeleteModel):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='Novel', related_name='roles')
    character_dynamics = models.CharField(max_length=500, verbose_name='Character Dynamics/角色动力学')
    name = models.CharField(max_length=100, verbose_name='Name/名字')
    identity_background = models.CharField(max_length=1000, verbose_name='Identity Background/身份背景')
    appearance = models.CharField(max_length=300, verbose_name='Appearance/外貌')
    character = models.CharField(max_length=500, verbose_name='Character/性格')
    values_beliefs = models.CharField(max_length=500, verbose_name='Values Beliefs/价值观与信念')
    core_traits = models.CharField(max_length=500, verbose_name='Core Traits/核心特质')
    motivation = models.CharField(max_length=500, verbose_name='Motivation/动机')
    growing_arc_light = models.CharField(max_length=500, verbose_name='Growing Arc Light/成长弧光')
    key_relationships = models.CharField(max_length=500, verbose_name='Key Relationships/关键关系')
