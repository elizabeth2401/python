import cv2
import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Inicializar geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

# Ubicación de la Catedral de Ciudad Guzmán (Señor San José) (ejemplo)
tourist_spot = {
    "name": "Catedral de Ciudad Guzmán (Señor San José)",
    "coords": (19.703611, -103.463056)  # Coordenadas de la Catedral de Ciudad Guzmán
}

def get_location():
    # Simular la obtención de la ubicación actual del usuario
    # Aquí se usa una ubicación cercana a la Catedral de Ciudad Guzmán
    return (19.703611, -103.463056)  # Cerca de la Catedral de Ciudad Guzmán

def draw_overlay(frame, text, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, position, font, 1, (255, 0, 0), 2, cv2.LINE_AA)

def main():
    cap = cv2.VideoCapture(0)
    current_location = get_location()
    distance = geodesic(current_location, tourist_spot["coords"]).meters
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if distance < 100:  # Si el usuario está a menos de 100 metros
            draw_overlay(frame, f"Estas cerca de: {tourist_spot['name']}", (10, 50))
        
        cv2.imshow('RA Geolocalizada', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

 
