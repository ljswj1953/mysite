# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FangWenQingKuang(models.Model):
    id = models.BigAutoField(primary_key=True)
    ri_qi = models.DateTimeField(blank=True, null=True)
    shang_pin_id = models.BigIntegerField()
    zhuang_tai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fang_wen_qing_kuang'
        unique_together = (('id', 'shang_pin_id'),)


class LeiMuDuiZhao(models.Model):
    id = models.AutoField(primary_key=True)
    lei_mu_yuan = models.CharField(max_length=50, blank=True, null=True)
    lei_mu = models.CharField(max_length=50, blank=True, null=True)
    web_lei_mu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei_mu_dui_zhao'


class ShangPinShuJu(models.Model):
    id = models.BigAutoField(primary_key=True)
    shang_pin_id = models.BigIntegerField()
    shang_pin_ming_cheng = models.CharField(max_length=100, blank=True, null=True)
    tu_pian_di_zhi = models.CharField(max_length=200, blank=True, null=True)
    shang_pin_lei_mu = models.CharField(max_length=50, blank=True, null=True)
    tao_di_zhi = models.CharField(max_length=400, blank=True, null=True)
    jia_ge = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    yue_xiao_liang = models.IntegerField(blank=True, null=True)
    yong_jin = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shou_ru_bi_lv = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quan_mian_e = models.IntegerField(blank=True, null=True)
    kai_shi = models.DateField(blank=True, null=True)
    jie_shu = models.DateField(blank=True, null=True)
    quan_di_zhi = models.CharField(max_length=400, blank=True, null=True)
    tian_jia_ri_qi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shang_pin_shu_ju'
        unique_together = (('id', 'shang_pin_id'),)
