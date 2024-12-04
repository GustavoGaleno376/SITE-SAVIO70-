import streamlit as st
import datetime

# Inicializando as reservas no session_state
if "reservations" not in st.session_state:
    st.session_state.reservations = []

if "usu_reserv" not in st.session_state or not st.session_state.usu_reserv.get("nome"):
    st.warning("Você precisa se cadastrar antes de acessar as reservas.")
    st.stop()

# Função para exibir as fotos das salas
def show_room_photo(room_name):
    room_photos = {
        "Auditório": "https://example.com/auditorio.jpg",  # Substitua com o URL da foto real
        "Laboratório": "https://example.com/laboratorio.jpg",
        "Biblioteca": "https://example.com/biblioteca.jpg",
        "Sala ds1": "https://example.com/sala_ds1.jpg",
        "Sala sist1": "https://example.com/sala_sist1.jpg",
        "Sala agn1": "https://example.com/sala_agn1.jpg",
        "Sala adm1": "https://example.com/sala_adm1.jpg",
    }
    return room_photos.get(room_name, "")

# Sidebar para navegação entre páginas
page = st.sidebar.selectbox("Escolha uma página", ["Fazer Reserva", "Minhas Reservas"])

if page == "Fazer Reserva":
    st.title("Controle de Reservas")
    st.write(f"Bem-vindo(a), {st.session_state.usu_reserv['nome']}!")

    # Lista de salas disponíveis
    available_rooms = [
        "Auditório",
        "Laboratório",
        "Biblioteca",
        "Sala ds1",
        "Sala sist1",
        "Sala agn1",
        "Sala adm1",
    ]

    # Mostrando reservas existentes
    if st.session_state.reservations:
        st.subheader("Reservas Feitas:")
        for res in st.session_state.reservations:
            st.write(
                f"Sala: {res['room']} - Data: {res['date']} - Horário: {res['time']} - Motivo: {res['reason']}"
            )
    else:
        st.write("Nenhuma reserva feita ainda.")

    # Formulário para nova reserva
    st.subheader("Nova Reserva")
    room = st.selectbox("Escolha uma sala", available_rooms)
    date = st.date_input("Escolha a data", min_value=datetime.date.today())
    motivo = st.text_input("Diga o motivo")
    time_input = st.text_input("Digite o horário (formato HH:MM)", "09:00")

    # Validando e processando a reserva
    try:
        time = datetime.datetime.strptime(time_input, "%H:%M").time()
    except ValueError:
        st.warning("Formato de hora inválido! Utilize o formato HH:MM (ex: 14:30).")
        time = None

    if st.button("Reservar"):
        if time:
            reservation_exists = any(
                res["room"] == room and res["date"] == str(date) and res["time"] == str(time)
                for res in st.session_state.reservations
            )

            if reservation_exists:
                st.warning("Esta sala já está reservada nesse horário.")
            else:
                st.session_state.reservations.append(
                    {"room": room, "date": str(date), "time": str(time), "reason": motivo}
                )
                st.success(f"Sala {room} reservada para {date} às {time}. Motivo: {motivo}")
        else:
            st.warning("Por favor, insira uma hora válida.")

elif page == "Minhas Reservas":
    st.title("Minhas Reservas")

    # Exibindo as reservas com fotos
    if st.session_state.reservations:
        st.subheader("Reservas Feitas:")
        for res in st.session_state.reservations:
            room_photo = show_room_photo(res['room'])
            st.write(f"Sala: {res['room']} - Data: {res['date']} - Hora: {res['time']} - Motivo: {res['reason']}")
            if room_photo:
                st.image(room_photo, caption=res['room'], use_container_width=True)
    else:
        st.write("Nenhuma reserva feita ainda.")
