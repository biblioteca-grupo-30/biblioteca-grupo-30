from rest_framework import permissions
from django.utils import timezone
from .models import Loan


class IsNotBlocked(permissions.BasePermission):
    message = "Usuário bloqueado. Não é \
possível criar ou atualizar empréstimos."

    def has_permission(self, request, view):
        user_id = request.data.get("user", request.user.id)
        loans = Loan.objects.filter(user_id=user_id)
        for loan in loans:
            if (loan.returned_date is None and
                    loan.blocked_until > timezone.now()):
                return False
        return True
