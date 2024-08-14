from django.contrib.auth.models import User
from utils import custom_upload_to, custom_upload_to_marriage

from django.db import models
from travelers.models import TravelerRecord

from utils import TimestampMixin, UserStampedMixin


# Create your models here.
class RefugeeId(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    refugee_id = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class FamilyAttestation(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    family_attestation = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class BirthCertificate(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    birth_certificate = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class NationalID(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    national_id = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class WeddingCertificate(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    wedding_certificate = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class EmbassyDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    embassy_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class MedicalDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    medical_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class OtherDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    other_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class MarriageRecord(TimestampMixin, UserStampedMixin, models.Model):

    CLASSIFICATION_CHOICES = [
        ('1', 'Civil/ሲቪል'),
        ('2', 'Christian/ክርስትያን'),
        ('3', 'Muslim/ምስልምና'),
        ('4', 'Hindu/ሂንዱ'),
        ('5', 'Customary/ባህላዊ'),
        ('6', 'Registered/ናይ መንግስ'),
    ]

    STATUS_CHOICES = [
        ('1', 'Initiated/ተበጊሱ'),
        ('2', 'Assigned/ተመዲቡ'),
        ('3', 'In Progress/ኣብ መስርሕ'),
        ('4', 'Completed/ተዛዚሙ'),
        ('5', 'Cancelled/ተሰሪዙ'),
    ]

    # Metadata
    requestor = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    marriage_classification = models.CharField(max_length=1, choices=CLASSIFICATION_CHOICES, null=True)
    requested_date = models.DateField(auto_now_add=True)
    marriage_planned_date = models.DateField(blank=True, null=True)
    record_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1',)
    assigned_officer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="person_assigned_marriage")
    officer_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class MarriageAttachments(TimestampMixin, UserStampedMixin, models.Model):
    record_id = models.ForeignKey(MarriageRecord, on_delete=models.PROTECT)
    passport_photo_bridegroom = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_photo_bride = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_photo_witness1 = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_photo_witness2 = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_or_id_bridegroom = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_or_id_bride = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_or_id_witness1 = models.ImageField(upload_to=custom_upload_to_marriage)
    passport_or_id_witness2 = models.ImageField(upload_to=custom_upload_to_marriage)
    lc1_letter = models.ImageField(upload_to=custom_upload_to_marriage)
    marriage_related_document_bridegroom = models.ImageField(upload_to=custom_upload_to_marriage)
    marriage_related_document_bride = models.ImageField(upload_to=custom_upload_to_marriage)
    proof_of_payment = models.ImageField(upload_to=custom_upload_to_marriage)
    birth_certificate = models.ImageField(upload_to=custom_upload_to_marriage)
    other_document = models.ImageField(upload_to=custom_upload_to_marriage)

    def count_non_null_fields(self):
        return sum(1 for field in self._meta.get_fields()
                   if isinstance(field, models.ImageField) and getattr(self, field.name))

    def __str__(self):
        return str(self.record_id.id)

