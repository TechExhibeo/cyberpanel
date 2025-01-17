from django.conf.urls import url
import views

urlpatterns = [
    url(r'^createBackup$', views.createBackup, name='createBackupInc'),
    url(r'^backupDestinations$', views.backupDestinations, name='backupDestinationsInc'),
    url(r'^addDestination$', views.addDestination, name='addDestinationInc'),
    url(r'^populateCurrentRecords$', views.populateCurrentRecords, name='populateCurrentRecordsInc'),
    url(r'^removeDestination$', views.removeDestination, name='removeDestinationInc'),
    url(r'^fetchCurrentBackups$', views.fetchCurrentBackups, name='fetchCurrentBackupsInc'),
    url(r'^submitBackupCreation$', views.submitBackupCreation, name='submitBackupCreationInc'),
    url(r'^getBackupStatus$', views.getBackupStatus, name='getBackupStatusInc'),
    url(r'^deleteBackup$', views.deleteBackup, name='deleteBackupInc'),
    url(r'^fetchRestorePoints$', views.fetchRestorePoints, name='fetchRestorePointsInc'),
    url(r'^restorePoint$', views.restorePoint, name='restorePointInc'),
    url(r'^scheduleBackups$', views.scheduleBackups, name='scheduleBackupsInc'),
    url(r'^submitBackupSchedule$', views.submitBackupSchedule, name='submitBackupScheduleInc'),
    url(r'^scheduleDelete$', views.scheduleDelete, name='scheduleDeleteInc'),
    url(r'^getCurrentBackupSchedules$', views.getCurrentBackupSchedules, name='getCurrentBackupSchedulesInc'),
]