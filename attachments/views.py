from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.apps import apps
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .att_dec import handle_file_upload, delete_file
from .models import RefugeeId, FamilyAttestation, BirthCertificate, NationalID, WeddingCertificate, EmbassyDocument, MedicalDocument, OtherDocument, MarriageRecord, MarriageAttachments
from decorators import authentication_required, allowed_users
from travelers.models import TravelerRecord


# Marriage related CRUD
@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def marriage_documents(request):

    rec = MarriageRecord.objects.filter(requestor=request.user)
    att = MarriageAttachments.objects.all()

    return render(request, 'marriage_attachment.html', {
        'rec': rec,
        'att': att,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def add_marriage_record(request):
    if request.method == "POST":
        requestor = request.user
        marriage_classification = request.POST.get('marriage_classification')
        marriage_planned_date = request.POST.get('marriage_planned_date')

        # Create and save the MarriageRecord instance
        marriage_record = MarriageRecord(
            requestor=requestor,
            marriage_classification=marriage_classification,
            marriage_planned_date=marriage_planned_date,

        )
        marriage_record.save()

        messages.success(request, 'Record Added successfully.')
        return redirect('marriage_documents')

    return render(request, 'add_marriage_record.html', {})


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def add_marriage_attachment(request, record_id):
    rec = get_object_or_404(MarriageRecord, id=record_id)
    att, created = MarriageAttachments.objects.get_or_create(record_id=rec)

    return render(request, 'add_marriage_attachment.html', {
        'rec': rec,
        'att': att,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_photo_bridegroom')
def upload_passport_photo_bridegroom(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_photo_bride')
def upload_passport_photo_bride(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_photo_witness1')
def upload_passport_photo_witness1(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_photo_witness2')
def upload_passport_photo_witness2(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_or_id_bridegroom')
def upload_passport_or_id_bridegroom(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_or_id_bride')
def upload_passport_or_id_bride(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_or_id_witness1')
def upload_passport_or_id_witness1(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('passport_or_id_witness2')
def upload_passport_or_id_witness2(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('lc1_letter')
def upload_lc1_letter(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('marriage_related_document_bridegroom')
def upload_marriage_related_document_bridegroom(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('marriage_related_document_bride')
def upload_marriage_related_document_bride(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('proof_of_payment')
def upload_proof_of_payment(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('birth_certificate')
def upload_birth_certificate(request, record_id):
    pass


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
@csrf_exempt
@handle_file_upload('other_document')
def upload_other_document(request, record_id):
    pass


@delete_file('passport_photo_bridegroom')
def delete_passport_photo_bridegroom(request, record_id):
    pass


@delete_file('passport_photo_bride')
def delete_passport_photo_bride(request, record_id):
    pass


@delete_file('passport_photo_witness1')
def delete_passport_photo_witness1(request, record_id):
    pass


@delete_file('passport_photo_witness2')
def delete_passport_photo_witness2(request, record_id):
    pass


@delete_file('passport_or_id_bridegroom')
def delete_passport_or_id_bridegroom(request, record_id):
    pass


@delete_file('passport_or_id_bride')
def delete_passport_or_id_bride(request, record_id):
    pass


@delete_file('passport_or_id_witness1')
def delete_passport_or_id_witness1(request, record_id):
    pass


@delete_file('passport_or_id_witness2')
def delete_passport_or_id_witness2(request, record_id):
    pass


@delete_file('lc1_letter')
def delete_lc1_letter(request, record_id):
    pass


@delete_file('marriage_related_document_bridegroom')
def delete_marriage_related_document_bridegroom(request, record_id):
    pass


@delete_file('marriage_related_document_bride')
def delete_marriage_related_document_bride(request, record_id):
    pass


@delete_file('proof_of_payment')
def delete_proof_of_payment(request, record_id):
    pass


@delete_file('birth_certificate')
def delete_birth_certificate(request, record_id):
    pass


@delete_file('other_document')
def delete_other_document(request, record_id):
    pass

# END OF Marriage Related CRUD

@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def attach(request):

    ref_id_count = RefugeeId.objects.filter(traveler__user=request.user).count()
    fam_att_count = FamilyAttestation.objects.filter(traveler__user=request.user.id).count()
    bir_cer_count = BirthCertificate.objects.filter(traveler__user=request.user.id).count()
    nat_id_count = NationalID.objects.filter(traveler__user=request.user.id).count()
    wed_cer_count = WeddingCertificate.objects.filter(traveler__user=request.user.id).count()
    emb_doc_count = EmbassyDocument.objects.filter(traveler__user=request.user.id).count()
    med_doc_count = MedicalDocument.objects.filter(traveler__user=request.user.id).count()
    oth_doc_count = OtherDocument.objects.filter(traveler__user=request.user.id).count()

    ref_id = RefugeeId.objects.filter(traveler__user=request.user)
    fam_att = FamilyAttestation.objects.filter(traveler__user=request.user.id)
    bir_cer = BirthCertificate.objects.filter(traveler__user=request.user.id)
    nat_id = NationalID.objects.filter(traveler__user=request.user.id)
    wed_cer = WeddingCertificate.objects.filter(traveler__user=request.user.id)
    emb_doc = EmbassyDocument.objects.filter(traveler__user=request.user.id)
    med_doc = MedicalDocument.objects.filter(traveler__user=request.user.id)
    oth_doc = OtherDocument.objects.filter(traveler__user=request.user.id)

    return render(request, 'attachment.html', {
        'ref_id_count': ref_id_count,
        'fam_att_count': fam_att_count,
        'bir_cer_count': bir_cer_count,
        'nat_id_count': nat_id_count,
        'wed_cer_count': wed_cer_count,
        'emb_doc_count': emb_doc_count,
        'med_doc_count': med_doc_count,
        'oth_doc_count': oth_doc_count,

        'ref_id': ref_id,
        'fam_att': fam_att,
        'bir_cer': bir_cer,
        'nat_id': nat_id,
        'wed_cer': wed_cer,
        'emb_doc': emb_doc,
        'med_doc': med_doc,
        'oth_doc': oth_doc,

    })


# @authentication_required
# @allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
# def my_documents(request):
#
#     ref_id = RefugeeId.objects.filter(traveler__user=request.user)
#     fam_att = FamilyAttestation.objects.filter(traveler__user=request.user.id)
#     bir_cer = BirthCertificate.objects.filter(traveler__user=request.user.id)
#     nat_id = NationalID.objects.filter(traveler__user=request.user.id)
#     wed_cer = WeddingCertificate.objects.filter(traveler__user=request.user.id)
#     emb_doc = EmbassyDocument.objects.filter(traveler__user=request.user.id)
#     med_doc = MedicalDocument.objects.filter(traveler__user=request.user.id)
#     oth_doc = OtherDocument.objects.filter(traveler__user=request.user.id)
#
#     return render(request, 'my_documents.html', {
#         'ref_id': ref_id,
#         'fam_att': fam_att,
#         'bir_cer': bir_cer,
#         'nat_id': nat_id,
#         'wed_cer': wed_cer,
#         'emb_doc': emb_doc,
#         'med_doc': med_doc,
#         'oth_doc': oth_doc,
#
#     })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_ref_id(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = RefugeeId.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'refugee_id' in request.FILES:
            refugee_id_file = request.FILES['refugee_id']
            rec = RefugeeId(traveler=traveler, refugee_id=refugee_id_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'ref_id.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_fam_att(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = FamilyAttestation.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'family_attestation' in request.FILES:
            family_attestation_file = request.FILES['family_attestation']
            rec = FamilyAttestation(traveler=traveler, family_attestation=family_attestation_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'fam_att.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_bir_cer(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = BirthCertificate.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'birth_certificate' in request.FILES:
            birth_certificate_file = request.FILES['birth_certificate']
            rec = BirthCertificate(traveler=traveler, birth_certificate=birth_certificate_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'bir_cer.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_nat_id(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = NationalID.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'national_id' in request.FILES:
            national_id_file = request.FILES['national_id']
            rec = NationalID(traveler=traveler, national_id=national_id_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'nat_id.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_wed_cer(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = WeddingCertificate.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'wedding_certificate' in request.FILES:
            wedding_certificate_file = request.FILES['wedding_certificate']
            rec = WeddingCertificate(traveler=traveler, wedding_certificate=wedding_certificate_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'wed_cer.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_emb_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = EmbassyDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'embassy_document' in request.FILES:
            embassy_document_file = request.FILES['embassy_document']
            rec = EmbassyDocument(traveler=traveler, embassy_document=embassy_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'emb_doc.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_med_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = MedicalDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'medical_document' in request.FILES:
            medical_document_file = request.FILES['medical_document']
            rec = MedicalDocument(traveler=traveler, medical_document=medical_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'med_doc.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_oth_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = OtherDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'other_document' in request.FILES:
            other_document_file = request.FILES['other_document']
            rec = OtherDocument(traveler=traveler, other_document=other_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'oth_doc.html', {'attachment': attachment})


def generic_delete(request, model_name, pk):
    model = apps.get_model('attachments', model_name)
    rec = get_object_or_404(model, id=pk)
    rec.delete()
    messages.success(request, 'Record Deleted')

    referer_url = request.META.get('HTTP_REFERER', 'default_fallback_url')
    return redirect(referer_url)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_ref_id(request, pk):
    return generic_delete(request, 'RefugeeId', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_fam_att(request, pk):
    return generic_delete(request, 'FamilyAttestation', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_bir_cer(request, pk):
    return generic_delete(request, 'BirthCertificate', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_nat_id(request, pk):
    return generic_delete(request, 'NationalID', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_wed_cer(request, pk):
    return generic_delete(request, 'WeddingCertificate', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_emb_doc(request, pk):
    return generic_delete(request, 'EmbassyDocument', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_med_doc(request, pk):
    return generic_delete(request, 'MedicalDocument', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_oth_doc(request, pk):
    return generic_delete(request, 'OtherDocument', pk)
