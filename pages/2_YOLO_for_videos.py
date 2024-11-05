import streamlit as st
from yolo_predictions import YOLO_Pred
import cv2
import tempfile
import os

st.set_page_config(page_title="YOLO Video Object Detection", layout='wide', page_icon='./images/object.png')

st.header('Get Object Detection for any Video')
st.write('Please Upload Video to get detections')

with st.spinner('Please wait while your model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx', data_yaml='./models/data.yaml')

def upload_video():
    # Upload Video
    video_file = st.file_uploader(label='Upload Video', type=["mp4", "mkv", "avi"])
    if video_file is not None:
        file_details = {"filename": video_file.name,
                        "filetype": video_file.type,
                        "filesize": "{:,.2f} MB".format(video_file.size/(1024**2))}
        st.success('VALID VIDEO file type')
        return video_file, file_details
    else:
        st.error('Please upload a valid video file (mp4, mkv, avi)')
        return None, None

def process_video(video_file):
    # Save video to a temporary file
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    temp_video.write(video_file.read())
    temp_video.close()  # Close the temporary file after writing
    temp_video_path = temp_video.name

    # Open video for reading and prepare for output
    cap = cv2.VideoCapture(temp_video_path)
    output_path = "processed_video.mp4"  # Save to a fixed path during session
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    frame_skip = int(fps)  # Process every 1 second of frames
    frame_count = 0

    st.info("Processing video...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            pred_frame = yolo.predictions(frame)  # Get predictions for every nth frame
            out.write(pred_frame)  # Write frame with predictions
        else:
            out.write(frame)  # Write unprocessed frame for smoother playback

        frame_count += 1

    # Release the video objects before deleting temp file
    cap.release()
    out.release()
    os.remove(temp_video_path)  # Clean up the temporary file after processing

    return output_path

def main():
    video_file, details = upload_video()
    if video_file:
        st.json(details)
        if st.button('Start Detection'):
            with st.spinner("Processing video, this might take some time..."):
                output_path = process_video(video_file)
                st.success("Video processed successfully!")
                st.video(output_path)  # Display the saved output video

if __name__ == "__main__":
    main()
