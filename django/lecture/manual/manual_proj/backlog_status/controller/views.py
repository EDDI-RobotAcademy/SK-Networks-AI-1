from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_status.service.backlog_status_service_impl import BacklogStatusServiceImpl


class BacklogStatusView(viewsets.ViewSet):
    backlogStatusService = BacklogStatusServiceImpl.getInstance()

    def createBacklogStatus(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        status = data.get('status')

        createdBacklogStatus = self.backlogStatusService.createBacklogStatus(backlogId, status)

        return Response(createdBacklogStatus, status=status.HTTP_200_OK)

    def modifyBacklogStatus(self, request):
        data = request.data
        status = data.get('status')
        backlogId = data.get('backlogId')

        if not status:
            return Response({"error": "변경할 status 값이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            isSuccess = self.backlogStatusService.modifyBacklogStatus(backlogId, status)

            return Response(isSuccess, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
