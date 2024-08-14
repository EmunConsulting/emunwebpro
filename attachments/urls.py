from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('attach/', views.attach, name='attach'),
    # path('my_documents/', views.my_documents, name='my_documents'),
    path('add_ref_id/', views.add_ref_id, name='add_ref_id'),
    path('add_fam_att/', views.add_fam_att, name='add_fam_att'),
    path('add_bir_cer/', views.add_bir_cer, name='add_bir_cer'),
    path('add_nat_id/', views.add_nat_id, name='add_nat_id'),
    path('add_wed_cer/', views.add_wed_cer, name='add_wed_cer'),
    path('add_emb_doc/', views.add_emb_doc, name='add_emb_doc'),
    path('add_med_doc/', views.add_med_doc, name='add_med_doc'),
    path('add_oth_doc/', views.add_oth_doc, name='add_oth_doc'),

    # Delete
    path('del_ref_id/<int:pk>', views.del_ref_id, name='del_ref_id'),
    path('del_fam_att/<int:pk>', views.del_fam_att, name='del_fam_att'),
    path('del_bir_cer/<int:pk>', views.del_bir_cer, name='del_bir_cer'),
    path('del_nat_id/<int:pk>', views.del_nat_id, name='del_nat_id'),
    path('del_wed_cer/<int:pk>', views.del_wed_cer, name='del_wed_cer'),
    path('del_emb_doc/<int:pk>', views.del_emb_doc, name='del_emb_doc'),
    path('del_med_doc/<int:pk>', views.del_med_doc, name='del_med_doc'),
    path('del_oth_doc/<int:pk>', views.del_oth_doc, name='del_oth_doc'),

    # Marriage Related
    path('marriage_documents/', views.marriage_documents, name='marriage_documents'),
    path('add_marriage_record/', views.add_marriage_record, name='add_marriage_record'),
    path('add_marriage_attachment/<int:record_id>', views.add_marriage_attachment, name='add_marriage_attachment'),

    # Upload attachments related to marriage
    path('upload_passport_photo_bridegroom/<int:record_id>', views.upload_passport_photo_bridegroom, name='upload_passport_photo_bridegroom'),
    path('upload/passport_photo_bride/<int:record_id>/', views.upload_passport_photo_bride, name='upload_passport_photo_bride'),
    path('upload/passport_photo_witness1/<int:record_id>/', views.upload_passport_photo_witness1, name='upload_passport_photo_witness1'),
    path('upload/passport_photo_witness2/<int:record_id>/', views.upload_passport_photo_witness2, name='upload_passport_photo_witness2'),
    path('upload/passport_or_id_bridegroom/<int:record_id>/', views.upload_passport_or_id_bridegroom, name='upload_passport_or_id_bridegroom'),
    path('upload/passport_or_id_bride/<int:record_id>/', views.upload_passport_or_id_bride, name='upload_passport_or_id_bride'),
    path('upload/passport_or_id_witness1/<int:record_id>/', views.upload_passport_or_id_witness1, name='upload_passport_or_id_witness1'),
    path('upload/passport_or_id_witness2/<int:record_id>/', views.upload_passport_or_id_witness2, name='upload_passport_or_id_witness2'),
    path('upload/lc1_letter/<int:record_id>/', views.upload_lc1_letter, name='upload_lc1_letter'),
    path('upload/marriage_related_document_bridegroom/<int:record_id>/', views.upload_marriage_related_document_bridegroom, name='upload_marriage_related_document_bridegroom'),
    path('upload/marriage_related_document_bride/<int:record_id>/', views.upload_marriage_related_document_bride, name='upload_marriage_related_document_bride'),
    path('upload/proof_of_payment/<int:record_id>/', views.upload_proof_of_payment, name='upload_proof_of_payment'),
    path('upload/birth_certificate/<int:record_id>/', views.upload_birth_certificate, name='upload_birth_certificate'),
    path('upload/other_document/<int:record_id>/', views.upload_other_document, name='upload_other_document'),

    # Delete attachments related to marriage
    path('delete/passport_photo_bridegroom/<int:record_id>/', views.delete_passport_photo_bridegroom, name='delete_passport_photo_bridegroom'),
    path('delete/passport_photo_bride/<int:record_id>/', views.delete_passport_photo_bride, name='delete_passport_photo_bride'),
    path('delete/passport_photo_witness1/<int:record_id>/', views.delete_passport_photo_witness1, name='delete_passport_photo_witness1'),
    path('delete/passport_photo_witness2/<int:record_id>/', views.delete_passport_photo_witness2, name='delete_passport_photo_witness2'),
    path('delete/passport_or_id_bridegroom/<int:record_id>/', views.delete_passport_or_id_bridegroom, name='delete_passport_or_id_bridegroom'),
    path('delete/passport_or_id_bride/<int:record_id>/', views.delete_passport_or_id_bride, name='delete_passport_or_id_bride'),
    path('delete/passport_or_id_witness1/<int:record_id>/', views.delete_passport_or_id_witness1, name='delete_passport_or_id_witness1'),
    path('delete/passport_or_id_witness2/<int:record_id>/', views.delete_passport_or_id_witness2, name='delete_passport_or_id_witness2'),
    path('delete/lc1_letter/<int:record_id>/', views.delete_lc1_letter, name='delete_lc1_letter'),
    path('delete/marriage_related_document_bridegroom/<int:record_id>/', views.delete_marriage_related_document_bridegroom, name='delete_marriage_related_document_bridegroom'),
    path('delete/marriage_related_document_bride/<int:record_id>/', views.delete_marriage_related_document_bride, name='delete_marriage_related_document_bride'),
    path('delete/proof_of_payment/<int:record_id>/', views.delete_proof_of_payment, name='delete_proof_of_payment'),
    path('delete/birth_certificate/<int:record_id>/', views.delete_birth_certificate, name='delete_birth_certificate'),
    path('delete/other_document/<int:record_id>/', views.delete_other_document, name='delete_other_document'),

]