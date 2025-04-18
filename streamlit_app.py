import streamlit as st

# Formatting
st.set_page_config(
    page_title='NystagmusQuiz',
    layout='wide',
    page_icon=':grey_question:',
    initial_sidebar_state="collapsed",
)

st.sidebar.markdown("""
# Inhalt

- <font size="4">**[Quiz](#quiz)**</font>
- <font size="4">**[Quellen](#quellen)**</font>
- <font size="4">**[Danksagung](#danksagung)**</font>
- <font size="4">**[Haftungsausschluss](#haftungsausschluss)**</font>
- <font size="4">**[Links](#links)**</font>
""", unsafe_allow_html=True)

if __name__ == '__main__':
    # Handle session
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    # Remove space at top of page
    st.markdown('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

    # Header
    st.header("#", anchor="Einführung")
    st.title('Hast Du je von :blue[Nystagmus] gehört? ... Nystag Was?')

    st.markdown("Neugierig worum es sich hierbei handelt? Dann nimm Dir ein paar Minuten Zeit für "
                +"das nachfolgende Quiz. Aus den Antworten wirst Du etwas Neues lernen über das bis heute "
                +"nur sehr wenige Personen etwas wissen. "
                +"Versuche die richtige Auswahl zu treffen. Die richtige Antwort wird dann zusammen mit einer "
                +"Erläuterung angezeigt. "
                +"Feedback, wie Dir das Quiz gefallen hat und was verbessert werden kann, "
                +"gerne an nystag_quiz@gmail.com. **Viel Spaß!**", unsafe_allow_html=True)

    # Variable definitions
    frage1 = ""
    frage2 = list()
    frage3 = ""
    frage4 = ""
    frage5 = list()
    frage6 = ""

    st.header("Quiz")

    col1, col2= st.columns(2, gap="large")

    with col1:
        # Question 1"
        frage1 = st.radio(label="**1. Worum handelt es sich bei Nystagmus?**", options=('Keines davon', 'Kleinstadt in Griechenland', 'Rechengesetz der Algebra', 'Augenzittern'), index=0, horizontal=True)
        if frage1 == 'Kleinstadt in Griechenland':
            st.write('**:red[FALSCH]** Versuche es noch einmal.')
        elif frage1 == 'Rechengesetz der Algebra':
            st.write('**:red[FALSCH]** Versuche es noch einmal.')
        elif frage1 == 'Augenzittern':
            st.write('**:green[RICHTIG]**   Als Nystagmus bezeichnet man ein zittern der Augen.')
            st.write("Bei Betroffenen bewegen sich die Augen unbewusst, d.h. ohne dass man es möchte. " \
                    + "Es gibt Menschen mit Nystagmus, deren Augen sich horizontal, vertikal oder rotierend bewegen. "
                    + "Videos die zeigen, wie das aussieht, gibt es [hier](https://www.facebook.com/nystagmusnetzwerk/videos/).")
           
            st.write("Das Augenzittern, welches Nystagmus genannt wird, führt häufig zu einem teilweise beschränkten Sehvermögen. "
                    +" Viele Betroffene haben eine Sehschäche oder eine Sehbehinderung. Nach deutschem Richtlinien hat man ab 30 % "
                    +" Sehschärfe (mit Brille oder Kontaktlinsen) eine Sehbehinderung. Alles darüber gilt als Sehschwäche. Andere "
                    + "Faktoren wie Gesichtsfeldeinschänkungen können jedoch zusätzlich berücksichtigt werden. Nur wenige der von "
                    + "Nystagmus betroffenen Personen können Auto fahren und die meisten Betroffenen stoßen auf Schwierigkeiten im "
                    + "täglichen Leben, sowohl in praktischer als auch in gesellschaftlicher Hinsicht. Außerdem kommt es häufig zu "
                    + "Problemen in der Schule oder im Arbeitsleben.")
        else:
            pass

    with col2:
        if frage1 == "Augenzittern":
            # Question 2
            st.write("**2. Wodurch kann Nystagmus auftreten?**")
            option2a = st.checkbox("Angeboren - Erblich bedingt")
            option2b = st.checkbox("Angeboren - In Zusammenhang mit anderen Krankheiten")
            option2c = st.checkbox("Angeboren - Ohne ersichtlichen Grund")
            option2d = st.checkbox("Erworben - Plötzlich im Verlauf des Lebens")

            if option2a == True:
                frage2.append("Angeboren - Erblich bedingt")
            if option2b == True:
                frage2.append("Angeboren - In Zusammenhang mit anderen Krankheiten")
            if option2c == True:
                frage2.append("Angeboren - Ohne ersichtlichen Grund")
            if option2d == True:
                frage2.append("Erworben - Plötzlich im Verlauf des Lebens")

            if len(frage2) > 0:
                if "Angeboren - Erblich bedingt" in frage2:
                    st.write("**:green[RICHTIG]** Nystagmus kann erblich bedingt und bereits bei der Geburt vorhanden sein.")
                if "Angeboren - In Zusammenhang mit anderen Krankheiten" in frage2:
                    st.write("**:green[RICHTIG]** Nystagmus kann angeboren sein und dann in Verbindung mit anderen Krankheiten auftreten. "
                            +"Er kann mit Albinismus oder Grauem Star im Kindesalter zusammenhängen.")
                if "Angeboren - Ohne ersichtlichen Grund" in frage2:
                    st.write("**:green[RICHTIG]** Nystagmus kann bereits bei der Geburt auftreten, ohne dass ein Grund ersichtlich ist.")
                if "Erworben - Plötzlich im Verlauf des Lebens" in frage2:
                    st.write("**:green[RICHTIG]** Nystagmus kann im Verlaufe des Lebens auftreten, manchmal durch einen "
                            +"Unfall oder eine Krankheit (wie z.B. ein Schlaganfall, Multiple Sklerose oder das Arnold-Chiari-Syndrom).")
                    
                if len(frage2) < 4:
                    st.write("Nystagmus kann auch noch in anderer Form auftreten. **Versuche auch eine der anderen Auswahloptionen.**")


    # Some space here
    st.write('&nbsp;')

    # New columns for the next questions
    col3, col4= st.columns(2, gap="large")
    with col3:
        if len(frage2) == 4:
            st.write("**3. Wie häufig tritt Nystagmus auf?** Experten glauben, dass ca. ein Mensch "
                    +"von **:blue[AUSWAHL]** Menschen Nystagmus hat.")
        
            col3a, col3b, col3c = st.columns([0.5,10,2])
            with col3b:
                # Question 3
                frage3= st.slider("", 0, 1000, value=0, step=50)
        
                if frage3 == 0:
                    st.write("Regler nach rechts verschieben.")
                elif frage3 < 1000:
                    st.write("Nystagmus tritt weniger häufig auf.")
                else:
                    st.write("**:green[RICHTIG]**  Experten glauben, dass circa einer von 1000 Menschen Nystagmus hat.")
        
    with col4:
        col4a, col4b = st.columns(2, gap="medium")
        
        if frage3 == 1000:
            col4a, col4b = st.columns(2, gap="medium")
        
            with col4a:
                frage4 = st.radio(label="**4. Kann eine Brille gegen Nystagmus helfen?**", options=("Keines davon", "Ja", "Nein"), index=0)

                if frage4 == "Ja":
                    st.markdown("""<font size="6">**:red[FALSCH]**</font>""", unsafe_allow_html=True)
                if frage4 == "Nein":
                    st.markdown("""<font size="6">**:green[RICHTIG]**</font>""", unsafe_allow_html=True)

            with col4b:
                st.image(image="./brille.png", use_column_width=None, width=None)

            if frage4 == "Ja" or frage4 == "Nein":
                st.write("Es wird häufig von Laien angenommen, dass eine Brille gegen Nystagmus helfen würde, da viele Menschen mit Nystagmus "
                        +"kleine Druckschrift nur lesen können, wenn sie nahe genug sind oder eine Lesehilfe benutzen. "
                        +"Aber der Nystagmus selbst kann mit Brillen oder Kontaktlinsen NICHT korrigiert werden. Nur wenn zusätzlichen "
                        +"Augenkrankheiten bestehen, können sie helfen, um diese zu korrieren.", unsafe_allow_html=True)

    # Some space here
    st.write('&nbsp;')

    # New columns for the next questions
    col5, col6= st.columns(2, gap="large")
    with col5:
        if frage4 == "Ja" or frage4 == "Nein":
            frage5 = st.multiselect(label="**5. Wie äußert sich Nystagmus im Alltag?** Nystagmus beeinflusst:", 
                           options=("Lesegeschwindigkeit", "Reaktionsvermögen", "Entfernungen einzuschätzen",
                                    "Gleichgewichtssinn"), default=None)
      
            if(frage5 != None):
                if "Lesegeschwindigkeit" in frage5:
                    st.write("**:green[RICHTIG]** Das Lesen kann durch Nystagmus verlangsamt werden, da es länger dauert, die Schrift zu entziffern. "
                            +"Dies ist jedoch kein Zeichen von beschränkter Lesefähigkeit.")
                if "Reaktionsvermögen" in frage5: 
                    st.write("**:green[RICHTIG]** Menschen mit Nystagmus brauchen mehr Zeit, um etwas sehen und erkennen zu können als Menschen "
                        +"mit normaler Sehfähigkeit.")
                if "Entfernungen einzuschätzen" in frage5:
                    st.write("**:green[RICHTIG]** Augenzittern kann die Fähigkeit, genaue Entfernungen zu sehen beeinflussen und kann daher "
                        +"zum Stolpern oder zur Ungewandtheit beitragen. Viele Betroffene haben deshalb Probleme bei einigen Sportarten.")  
                if "Gleichgewichtssinn" in frage5:
                    st.write("**:green[RICHTIG]** Für manche Betroffene ist das Gleichgewicht ein Problem, deshalb sollten diese Treppen "
                            +"und unebene Flächen langsam betreten.")

    with col6:
        if len(frage5)>2:
            frage6 = st.radio(label="**6. Die Sehbeinträchtigung durch Nystagmus ist immer gleich.**", options=("Keines davon", "Korrekt", "Trifft nicht zu"), horizontal=True)
        
            if frage6 == "Korrekt":
                st.markdown("""<font size="4">**:red[FALSCH]**</font> Dies trifft nicht zu. Die Sehbeeinträchtigung kann in Abhängigkeit
                von der Situation sehr unterschiedlich sein.""", unsafe_allow_html=True)
            if frage6 == "Trifft nicht zu":
                st.markdown("""<font size="4">**:green[RICHTIG]**</font>""", unsafe_allow_html=True)

            if frage6 == "Korrekt" or frage6 == "Trifft nicht zu":
                st.markdown("""
                - Das Sehvermögen ändert sich im Laufe des Tages und mag von emotionalen sowie körperlichen Erscheinungen wie z.B. Ermüdung, Nervosität, Anspannung oder auch von dem Einfluss einer unbekannten Umgebung beeinträchtigt werden.
                - Der Sehwinkel ist von Bedeutung. Viele Betroffene können ihren Blick auf die eine oder andere Seite richten, so dass die Augenbewegungen verringert werden und das Sehvermögen besser wird. Diejenigen, die einen solchen 'Nullpunkt' haben, können eine Kopfstellung annehmen, welche es ihnen gestattet, ihr Sehvermögen bestens zu verwenden.
                - Schlechte Beleuchtung kann das Sehvermögen beeinträchtigen. Viele Betroffene sind zusätzlich lichtempfindlich."""
                , unsafe_allow_html=True)

    # Some space here
    st.write('&nbsp;')

    st.header("Quellen")
    st.write("Die Informationen auf dieser Webseite wurden aus folgenden Quellen zusammengetragen:")
    st.write("[1] Faktenblatt (deutsche Übersetzung von [2]), Nystagmus Netzwerk e.V., [Webseite](http://www.nystagmusnetzwerk.de), Kontakt: info@nystagmusnetzwerk.de")
    st.write("[2] Fact Sheet, Nystagmus Network 2014, [Webseite](https://nystagmusnetwork.org), Kontakt: info@nystagmusnet.org")
    st.write("[3] Inernetseite mit allgemeinen Informationen des Nystagmus Netzwerk e.V. https://nystagmusnetzwerk.de/allgemeine-infos/")
    st.write("[4] 10 Tipps und Fakten zu Nystagmus, Nystagmus Netzwerk e.V. 2022, [Link](https://nystagmusnetzwerk.de/wp-content/uploads/2022/06/Broschuere-10-Tipps-und-10-Fakten-zu-Nystagmus.pdf)")

    st.header("Danksagung")
    st.write("Die Erstellung dieser Webseite wäre nicht möglich gewesen ohne die von folgenden Institutionen bereitgestellten Informationen ")
    st.markdown("- :blue[Nystagmus Netzwerk e.V.]: Ehrenamtlich arbeitender Verein mit den Zielen: "
                +"1. Unterstützung der Vernetzung von Betroffenen und Familien. "
                +"2. Beratung von Betroffenen und Familien. "
                +"3. Öffentlichkeitsarbeit zur Sensibilisierung und Bildungsarbeit. "
                +"4. Erstellen und Verbreiten von frei zugänglichem Informationsmaterial. "
                +"5. Anregung und Organisation von Veranstaltungen. "
                +"6. Unterstützung von Forschungsvorhaben. [Weitere Informationen](http://www.nystagmusnetzwerk.de)")
                
    st.markdown("- :blue[Nystagmus Network (Großbritannien)]. Das Nystagmus Network (Großbritannien) ist eine  offizielle Wohltätigkeitsstiftung, "
               +"deren Aufgabe es ist, Kindern und Erwachsenen mit der Augenkrankheit Nystagmus durch Auskunft und Beratung hilfreich zur "
               +"Seite zu stehen. Des Weiteren bemüht sich die Stiftung Unterstützung für Forschungsarbeiten aufzubringen, die möglicherweise "
               +"zur Entwicklung von Heilverfahren führen. [Weitere Informationen](https://www.nystagmusnet.org)")
    st.write("Beiden Einrichtungen gebührt ein besonderer Dank für ihr Engagement und für ihre Bemühungen das Wissen über Nystagmus weiter "
            +"zu verbereiten. Möge diese Webseite ein wenig dazu beitragen das Wissen über Nystagmus in der Bevölkerung zu fördern!")
    
    st.header("Haftungsausschluss")
    st.write("Die Informationen auf dieser Webseite wurden den genannten Quellen entnommen und wurden sorgfältig recherchiert und sinngemäß übertragen. "
             +"Es kann dennoch keine Gewähr für die Informationen übernommen werden. Darüber hinaus ist zu beachten, dass eine Diagnose grundsätzlich "
             +"nur von Ärzten/-innen gestellt werden kann.")
    
    st.header("Links")
    st.markdown("""
    - Nystagmus Network Großbritannien: https://nystagmusnetwork.org
    - Nystagmus Netzwerk e.V.: http://www.nystagmusnetzwerk.de
    - Facebook Seite des Nystagmus Netzwerk e.V.: https://www.facebook.com/nystagmusnetzwerk
    - ANN: American Nystagmus Network: https://nystagmus.org
    """, unsafe_allow_html=True)

    # Define Style
    # Styling radio widget(s) - No preselection -> Hyde first (selected) button; Change font size
    st.markdown("""<style>div[role="radiogroup"] > :first-child{display: none !important; }</style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stRadio p {font-size:120%; !important; }</style>""", unsafe_allow_html=True)
    # Styling slider widget(s)
    st.markdown("""<style>.stSlider p {font-size:120%; !important; }</style>""", unsafe_allow_html=True)
    # Styling multiselect widget(s)
    st.markdown("""<style>.stMultiSelect p {font-size:120%; !important; }</style>""", unsafe_allow_html=True)

    col7a, col7b, col7c = st.columns(3, gap="medium")
    with col7b:
        st.markdown("*Author of webpage: Nadine Homeyer*")
