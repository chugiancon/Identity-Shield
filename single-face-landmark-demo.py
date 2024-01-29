import mediapipe as mp
import cv2 as cv

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(max_num_faces = 1, refine_landmarks = True, min_detection_confidence = 0.5,
                           min_tracking_confidence = 0.5) as face_mesh:
    while True:
        ret, frame = cap.read()

        result = face_mesh.process(frame)
        for face_landmarks in result.multi_face_landmarks:
            mp_drawing.draw_landmarks(image = frame,
                                      landmark_list = face_landmarks,
                                      connections = mp_face_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec = None,
                                      connection_drawing_spec = mp_drawing_styles
                                      .get_default_face_mesh_tesselation_style()
                                      )

        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break

cap.release()
cv.destroyAllWindows()