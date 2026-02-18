# REPLACE your urls.py with this corrected version:

from django.urls import path
from . import views

voice_interview_urls = [
    # Voice interview endpoints
    path('api/voice/start/', views.start_voice_interview, name='start_voice_interview'),
    path('api/voice/process/', views.process_voice_response, name='process_voice_response'),
    path('api/voice/status/<int:interview_id>/', views.get_voice_interview_status, name='get_voice_interview_status'),
    path('api/voice/end/', views.end_voice_interview, name='end_voice_interview'),
    
    
    # Optional: Admin endpoints for voice interview management
#    path('admin/voice/sessions/', views.admin_voice_sessions, name='admin_voice_sessions'),
 #   path('admin/voice/session/<int:session_id>/', views.admin_voice_session_detail, name='admin_voice_session_detail'),
]

urlpatterns = [
    path('', views.interview_interface, name='interview_interface'),
    # Interview management
    path('start/<int:interview_id>/', views.start_interview, name='start_interview'),
    # API endpoints for interview process
    path('api/save-audio/', views.save_audio_response, name='save_audio_response'),
    path('api/stream-frame/', views.stream_frame, name='stream_frame'),  # Real-time streaming
    path('api/upload-frames/', views.upload_video_frames, name='upload_video_frames'),  # Backward compatibility
    path('api/end/', views.end_interview, name='end_interview'),
    path('api/request-interview/', views.request_interview, name='request_interview'),
    path('api/current/', views.get_current_interview, name='get_current_interview'),
    # VIDEO RECORDING ENDPOINTS
    path('api/stream-video-chunk/', views.stream_video_chunk, name='stream_video_chunk'),
    path('api/finalize-video-session/', views.finalize_video_session, name='finalize_video_session'),
    path('api/kafka-video/<int:interview_id>/', views.get_kafka_video, name='get_kafka_video'),  # Handles both full video and chunks
    path('api/video-info/<int:interview_id>/', views.get_video_info, name='get_video_info'),
    path('api/video-manifest/<int:interview_id>/', views.get_video_manifest, name='get_video_manifest'),
    path('api/reconstructed-video/<int:interview_id>/', views.get_reconstructed_video, name='get_reconstructed_video'),
    path('api/download-video/<int:interview_id>/', views.download_video_file, name='download_video_file'),
    path('api/kafka-chunks/<str:session_id>/', views.get_kafka_chunks_direct, name='get_kafka_chunks_direct'),
    # REMOVED: path('api/video-chunk/<int:interview_id>/<int:chunk_number>/', views.get_video_chunk, name='get_video_chunk'),
    # Missing endpoint that frontend expects
    path('api/interviews/', views.get_all_interviews, name='get_all_interviews'),
    path('download-report/<int:interview_id>/', views.download_student_report, name='download_report'),

    # API endpoints for admin
    path('api/get_interviews_list/', views.get_interviews_list, name='get_interview_list'),
    path('api/interviews/<int:interview_id>/approve/', views.approve_interview, name='approve_interview'),
    path('api/interviews/<int:interview_id>/reject/', views.reject_interview, name='reject_interview'),
    # Interview status and data
    path('api/interviews/<int:interview_id>/status/', views.get_interview_status, name='get_interview_status'),
    path('api/interviews/<int:interview_id>/frames/', views.get_frame_status, name='get_frame_status'),
    path('api/interviews/<int:interview_id>/analysis/', views.get_frame_analysis, name='get_frame_analysis'),
    # Email notification endpoints
    path('api/interviews/<int:interview_id>/email-status/', views.get_email_notification_status, name='get_email_notification_status'),
    path('api/interviews/<int:interview_id>/trigger-email/', views.manually_trigger_email_notification, name='manually_trigger_email'),
    path('api/diagnostic/kafka/', views.diagnostic_kafka_status, name='diagnostic_kafka_status'),
    path('api/interviews/<int:interview_id>/create-session-json/', views.create_interview_session_json, name='create_interview_session_json'),
    path('api/test-hdfs/', views.test_hdfs_connection, name='test_hdfs_connection'),
    path('api/debug-hdfs-write/', views.debug_hdfs_write, name='debug_hdfs_write'),
    path('api/debug-audio-hdfs/', views.debug_audio_hdfs_write, name='debug_audio_hdfs_write'),
] + voice_interview_urls
