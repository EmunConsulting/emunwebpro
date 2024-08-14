from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import MultipleObjectsReturned
from django.views.decorators.csrf import csrf_exempt

from decorators import allowed_users
from .models import MarriageAttachments, MarriageRecord


def handle_file_upload(field_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, record_id, *args, **kwargs):
            if request.method == 'POST':
                file = request.FILES.get(field_name)
                record = get_object_or_404(MarriageRecord, id=record_id)

                try:
                    # Get or create the attachment instance
                    attachment, created = MarriageAttachments.objects.get_or_create(record_id=record)

                    # Update the specific field with the uploaded file
                    setattr(attachment, field_name, file)
                    attachment.save()

                    # Add success message
                    messages.success(request, f'{field_name.replace("_", " ").title()} uploaded successfully.')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                except MultipleObjectsReturned:
                    messages.error(request, 'Multiple attachments found for this record.')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                except Exception as e:
                    messages.error(request, f'An error occurred: {str(e)}')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            else:
                messages.error(request, 'Invalid request method.')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            # Redirect back to the referring page
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        return _wrapped_view
    return decorator


def delete_file(field_name):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        @allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
        @csrf_exempt
        def wrapped_view(request, record_id, *args, **kwargs):
            attachment = get_object_or_404(MarriageAttachments, record_id=record_id)
            file_field = getattr(attachment, field_name)

            if file_field:  # If the field is not empty
                file_field.delete(save=False)  # Clear the field without deleting the file
                attachment.save()  # Save the updated record
                messages.success(request, f'{field_name.replace("_", " ").title()} cleared successfully.')
            else:  # If the field is already empty
                messages.info(request, f'No file to clear for {field_name.replace("_", " ").title()}.')

            # Redirect back to the referring page
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        return wrapped_view
    return decorator