# -*- coding: utf-8 -*-
"""
Marathi translations for Dr. Gaikwad's Institute.

Keyed by the exact English string as it appears in the built HTML (whitespace
normalised). build.py walks each generated page and, wherever an element's text
matches a key here, writes the Marathi into a data-mr attribute. site.js swaps
textContent between the two on toggle.

Register note: the institute's own printed prospectus mixes Marathi with
transliterated English for technical terms (कोर्स, फी, हॉस्पिटल, पोस्टिंग,
स्टायपेंड). These translations follow that same register deliberately — it is
how the institute actually speaks to its students, and departing from it into
pure Sanskritised Marathi would read as stilted.

Proper nouns intentionally left in Latin script: hospital and laboratory names,
course codes (DMLT, DPC, DOTT, DOPTO, B.Voc, ADMLT), book titles, the institute
name, email and phone numbers.
"""

MR = {}

# ---------------------------------------------------------------- navigation
MR.update({
    "Home": "मुख्यपृष्ठ",
    "About": "आमच्याविषयी",
    "About & BSS": "आमच्याविषयी",
    "Courses": "कोर्सेस",
    "Fees & Stipend": "फी व स्टायपेंड",
    "Fees & Stipend": "फी व स्टायपेंड",
    "Admissions": "प्रवेश",
    "Placements": "नोकरी",
    "Gallery": "गॅलरी",
    "Contact": "संपर्क",
    "Apply Now": "अर्ज करा",          # kept short: the header row overflows on mobile otherwise
    "Menu": "मेनू",
    "Close": "बंद करा",
    "Skip to content": "मजकुरावर जा",
})

# ---------------------------------------------------------------- buttons / CTAs
MR.update({
    "View Courses & Fees": "कोर्सेस व फी पहा",
    "Talk to a Counsellor": "समुपदेशकाशी बोला",
    "Message on WhatsApp": "व्हॉट्सअ‍ॅपवर संदेश पाठवा",
    "WhatsApp Us": "आम्हाला व्हॉट्सअ‍ॅप करा",
    "WhatsApp us": "आम्हाला व्हॉट्सअ‍ॅप करा",
    "Chat on WhatsApp": "व्हॉट्सअ‍ॅपवर चॅट करा",
    "Or message on WhatsApp": "किंवा व्हॉट्सअ‍ॅपवर संदेश पाठवा",
    "Call the Institute": "संस्थेला फोन करा",
    "Call the institute": "संस्थेला फोन करा",
    "Download Prospectus (PDF)": "प्रॉस्पेक्टस डाउनलोड करा (PDF)",
    "Course details": "कोर्सची माहिती",
    "How to apply": "अर्ज कसा करावा",
    "Ask about this course": "या कोर्सबद्दल विचारा",
    "Arrange a visit": "भेटीची वेळ ठरवा",
    "Arrange a counselling visit": "समुपदेशन भेटीची वेळ ठरवा",
    "Browse courses": "कोर्सेस पहा",
    "Start your enquiry": "चौकशी सुरू करा",
    "Send enquiry": "चौकशी पाठवा",
    "Meet the Founder": "संस्थापकांविषयी",
    "Our Accreditations": "आमच्या मान्यता",
    "Our accreditations": "आमच्या मान्यता",
    "About the Institute": "संस्थेविषयी",
    "See Our Placements": "आमच्या नोकरीच्या संधी पहा",
    "Message the institute": "संस्थेला संदेश पाठवा",
    "Open in Google Maps": "गूगल मॅप्समध्ये उघडा",
    "Get directions": "रस्ता दाखवा",
    "Full fee schedule for every course": "प्रत्येक कोर्सचे संपूर्ण फी वेळापत्रक",
    "Full admission process & document checklist": "संपूर्ण प्रवेश प्रक्रिया व कागदपत्रांची यादी",
    "Read the refund policy in full": "फी परतावा नियम संपूर्ण वाचा",
    "About the degree pathway": "पदवी मार्गाविषयी",
    "Eligibility and full details": "पात्रता व संपूर्ण माहिती",
    "More about postings and placement": "पोस्टिंग व नोकरीविषयी अधिक",
    "See the certificates": "प्रमाणपत्रे पहा",
    "See the certificates →": "प्रमाणपत्रे पहा →",
    "Read about the founder →": "संस्थापकांविषयी वाचा →",
    "See all twelve courses →": "बारा कोर्सेस पहा →",
    "See the degree pathway →": "पदवी मार्ग पहा →",
    "See the twelve courses →": "बारा कोर्सेस पहा →",
    "About the degree pathway →": "पदवी मार्गाविषयी →",
    "View full letter": "संपूर्ण पत्र पहा",
})

# ---------------------------------------------------------------- eyebrow labels
MR.update({
    "Programmes": "कोर्सेस",
    "Certification Authority": "प्रमाणन संस्था",
    "Certification": "प्रमाणन",
    "Accreditation": "मान्यता",
    "Who we are": "आम्ही कोण आहोत",
    "The course": "कोर्सविषयी",
    "The process": "प्रक्रिया",
    "Checklist": "कागदपत्रांची यादी",
    "Key dates": "महत्त्वाच्या तारखा",
    "At a glance": "थोडक्यात",
    "Before you sign": "सही करण्यापूर्वी",
    "The institute": "संस्था",
    "Track one": "गट एक",
    "Track two": "गट दोन",
    "Track three": "गट तीन",
    "Degree programmes": "पदवी कोर्सेस",
    "Diploma courses": "डिप्लोमा कोर्सेस",
    "Certificate courses": "सर्टिफिकेट कोर्सेस",
    "Instalment dates": "हप्त्यांच्या तारखा",
    "Included in the fee": "फीमध्ये समाविष्ट",
    "The arithmetic": "हिशोब",
    "Stipend ladder": "स्टायपेंड वाढ",
    "Recognition": "सन्मान",
    "Written by the founder": "संस्थापकांनी लिहिलेली पुस्तके",
    "Founder & Director": "संस्थापक व संचालक",
    "Founder & Director": "संस्थापक व संचालक",
    "Community health": "सार्वजनिक आरोग्य",
    "Campus life": "संस्थेतील जीवन",
    "Cultural": "सांस्कृतिक",
    "Convocation": "पदवीदान समारंभ",
    "Training": "प्रशिक्षण",
    "Practical": "प्रात्यक्षिक",
    "On duty": "कामावर",
    "On posting": "पोस्टिंगवर",
    "Our students": "आमचे विद्यार्थी",
    "Where": "कुठे",
    "Supervision": "देखरेख",
    "On completion": "कोर्स पूर्ण झाल्यावर",
    "Requirement": "अट",
    "Flexibility": "सोय",
    "Payment": "फी भरणा",
    "Process": "प्रक्रिया",
    "Documents": "कागदपत्रे",
    "Postings": "पोस्टिंग",
    "Refund policy": "फी परतावा नियम",
    "Admission enquiry": "प्रवेश चौकशी",
    "Admissions Enquiry": "प्रवेश चौकशी",
    "Visit us": "आम्हाला भेट द्या",
    "Visit the institute": "संस्थेला भेट द्या",
    "Finding us": "आम्हाला कसे शोधाल",
    "Certificates": "प्रमाणपत्रे",
    "In their words": "त्यांच्या शब्दांत",
    "Where our graduates work": "आमचे विद्यार्थी कुठे काम करतात",
    "Where our students work": "आमचे विद्यार्थी कुठे काम करतात",
    "How the posting works": "पोस्टिंग कशी चालते",
    "For working technicians": "कार्यरत टेक्निशियनसाठी",
    "Degree pathway": "पदवी मार्ग",
    "Recommended route": "शिफारस केलेला मार्ग",
    "Why lateral entry matters": "लॅटरल एंट्रीचा फायदा",
    "Competitions & sports": "स्पर्धा व क्रीडा",
    "Competitions & sports": "स्पर्धा व क्रीडा",
    "Silver Jubilee": "रौप्य महोत्सव",
    "Classroom": "वर्ग",
    "Parade": "संचलन",
    "March past": "संचलन",
    "Annual day": "वार्षिक स्नेहसंमेलन",
    "Picnic": "सहल",
    "Community": "समाजसेवा",
    "Cooking": "पाककला",
    "Mehendi": "मेहंदी",
    "Hair styling": "केशरचना",
    "Contest": "स्पर्धा",
    "Marathon": "मॅरेथॉन",
    "Athletics": "मैदानी खेळ",
    "Sports day": "क्रीडा दिन",
    "Kabaddi": "कबड्डी",
    "Pulse Polio": "पल्स पोलिओ",
    "Covid-19": "कोविड-१९",
    "Award": "पुरस्कार",
    "Citation": "प्रशस्तिपत्र",
    "Certificate": "प्रमाणपत्र",
    "Photograph": "छायाचित्र",
    "Map": "नकाशा",
})

# ---------------------------------------------------------------- table headers
MR.update({
    "Diploma": "डिप्लोमा",
    "Eligibility": "पात्रता",
    "Duration": "कालावधी",
    "Course Fee": "कोर्स फी",
    "Course fee": "कोर्स फी",
    "Stipend (approx.)": "स्टायपेंड (अंदाजे)",
    "Placement": "नोकरी",
    "Stipend": "स्टायपेंड",
    "Fee & instalments": "फी व हप्ते",
    "Certificate / Diploma": "सर्टिफिकेट / डिप्लोमा",
    "Programme": "कोर्स",
    "Total fee": "एकूण फी",
    "Stage": "टप्पा",
    "Due by": "अंतिम तारीख",
    "Document": "कागदपत्र",
    "Copies": "प्रती",
    "Course": "कोर्स",
    "Assured": "हमी",
    "Non-stipendiary": "स्टायपेंड नाही",
    "At admission": "प्रवेशाच्या वेळी",
    "Then monthly": "नंतर दरमहा",
    "Location": "ठिकाण",
    "Founded": "स्थापना",
    "Years teaching": "वर्षे अध्यापन",
    "Students placed": "नोकरी मिळालेले विद्यार्थी",
    "Diploma duration": "डिप्लोमा कालावधी",
    "Posting radius": "पोस्टिंग क्षेत्र",
    "Qualifications": "शैक्षणिक पात्रता",
    "Manuals written": "लिहिलेली पुस्तके",
    "Civil defence": "नागरी संरक्षण",
    "Founded the institute": "संस्थेची स्थापना",
    "Months": "महिने",
    "Typical stipend": "नेहमीचा स्टायपेंड",
    "Telephone": "दूरध्वनी",
    "Alternate": "पर्यायी",
    "Address": "पत्ता",
    "Email": "ईमेल",
    "Nearest station": "जवळचे स्टेशन",
    "Dadar": "दादर",
    "per month": "दरमहा",
    "Enquiries open": "चौकशी सुरू",
    "Main intake": "मुख्य प्रवेश",
    "Late admission cutoff": "उशिरा प्रवेशाची अंतिम तारीख",
    "Posting begins": "पोस्टिंग सुरू",
    "Year round": "वर्षभर",
    "Months on posting": "पोस्टिंगचे महिने",
    "Years of practice": "वर्षांचा अनुभव",
    "BSS established": "बी.एस.एस. स्थापना",
    "Quality management": "गुणवत्ता व्यवस्थापन",
    "HLACT accreditation": "एचएलएसीटी मान्यता",
    "Courses": "कोर्सेस",
    "Year each": "प्रत्येकी एक वर्ष",
    "Fee each": "प्रत्येकी फी",
    "Diploma courses": "डिप्लोमा कोर्सेस",
    "Certificate courses": "सर्टिफिकेट कोर्सेस",
    "Degree pathways": "पदवी मार्ग",
    "Events a year": "वर्षातील कार्यक्रम",
    "Days of convocation": "पदवीदान दिवस",
    "Years of batches": "वर्षांच्या बॅचेस",
    "Lowest diploma fee": "सर्वात कमी डिप्लोमा फी",
    "Highest diploma fee": "सर्वाधिक डिप्लोमा फी",
})

# ---------------------------------------------------------------- form fields
MR.update({
    "Student name": "विद्यार्थ्याचे नाव",
    "Mobile number": "मोबाईल नंबर",
    "Email address": "ईमेल पत्ता",
    "Course of interest": "कोणता कोर्स करायचा आहे",
    "Last examination passed": "शेवटची उत्तीर्ण परीक्षा",
    "Area of residence": "राहण्याचा भाग",
    "Anything you would like to ask": "तुम्हाला काही विचारायचे आहे का",
    "10th — passed": "१० वी — उत्तीर्ण",
    "10th — failed": "१० वी — अनुत्तीर्ण",
    "12th — passed": "१२ वी — उत्तीर्ण",
    "12th — failed": "१२ वी — अनुत्तीर्ण",
    "Graduate": "पदवीधर",
    "Currently working in healthcare": "सध्या आरोग्यसेवेत कार्यरत",
    "Not sure — please advise": "निश्चित नाही — कृपया मार्गदर्शन करा",
    "One-year certificate course": "एक वर्षाचा सर्टिफिकेट कोर्स",
    "B.Voc / Advanced Diploma": "B.Voc / अ‍ॅडव्हान्स्ड डिप्लोमा",
    "We use your details only to respond to this enquiry.":
        "तुमची माहिती फक्त या चौकशीला उत्तर देण्यासाठी वापरली जाईल.",
})

# ---------------------------------------------------------------- eligibility values
MR.update({
    "10th pass or fail": "१० वी पास किंवा नापास",
    "12th pass or fail": "१२ वी पास किंवा नापास",
    "10th pass": "१० वी पास",
    "12th pass": "१२ वी पास",
    "10th": "१० वी",
    "12th": "१२ वी",
    "1 year": "१ वर्ष",
    "1 Year": "१ वर्ष",
    "4 + 20 months": "४ + २० महिने",
    "4 + 20 mo": "४ + २० महिने",
    "4 + 20": "४ + २०",
    "3 years · 6 sem.": "३ वर्षे · ६ सत्रे",
    "2 years · 4 sem.": "२ वर्षे · ४ सत्रे",
    "12th pass (60% and above)": "१२ वी पास (६०% व अधिक)",
    "12th pass + BSS diploma": "१२ वी पास + बी.एस.एस. डिप्लोमा",
    "On the day": "त्याच दिवशी",
    "Full fee complete": "संपूर्ण फी भरणे",
    "Cumulative total": "एकत्रित रक्कम",
})

# ---------------------------------------------------------------- footer
MR.update({
    "Institute": "संस्था",
    "Admission Process": "प्रवेश प्रक्रिया",
    "Placements & Postings": "नोकरी व पोस्टिंग",
    "Refund Policy": "फी परतावा नियम",
    "Contact & Directions": "संपर्क व पत्ता",
    "Gallery & Campus Life": "गॅलरी व संस्थेतील जीवन",
    "Accreditation": "मान्यता",
    "Fees & Stipend": "फी व स्टायपेंड",
    "Patient Care (DPC / DPCA)": "पेशंट केअर (DPC / DPCA)",
    "Medical Lab Technology (DMLT)": "मेडिकल लॅब टेक्नॉलॉजी (DMLT)",
    "Operation Theatre (DOTT)": "ऑपरेशन थिएटर (DOTT)",
    "Optometry (DOPTO)": "ऑप्टोमेट्री (DOPTO)",
    "Certificate Courses": "सर्टिफिकेट कोर्सेस",
    "B.Voc & ADMLT": "B.Voc व ADMLT",
    "All rights reserved.": "सर्व हक्क राखीव.",
})

# ---------------------------------------------------------------- shared chrome (page-wide)
MR.update({
    "Paramedical Training · Dadar, Mumbai": "पॅरामेडिकल प्रशिक्षण · दादर, मुंबई",
    "203 Akanksha, Opposite Plaza,": "२०३ आकांक्षा, प्लाझा समोर,",
    "203 Akanksha, Opp. Plaza,": "२०३ आकांक्षा, प्लाझा समोर,",
    "Dadar (West), Mumbai 400 028": "दादर (प), मुंबई ४०० ०२८",
    "Dadar (W), Mumbai 400 028": "दादर (प), मुंबई ४०० ०२८",
    "203 Akanksha, Opp. Plaza, Dadar (W), Mumbai 400 028":
        "२०३ आकांक्षा, प्लाझा समोर, दादर (प), मुंबई ४०० ०२८",
    "Maharashtra, India": "महाराष्ट्र, भारत",
    "Fees": "फी",
    "Diploma Courses": "डिप्लोमा कोर्सेस",
    "Placements & Postings": "नोकरी व पोस्टिंग",
    "Gallery & Campus Life": "गॅलरी व संस्थेतील जीवन",
    "Contact & Directions": "संपर्क व पत्ता",
    "About & BSS Certification": "आमच्याविषयी व बी.एस.एस. प्रमाणन",
    "B.Voc & ADMLT": "B.Voc व ADMLT",
    "Important disclosures.": "महत्त्वाची सूचना.",
    "© 2026 Dr. Gaikwad's Institute. All rights reserved.":
        "© २०२६ डॉ. गायकवाड्स इन्स्टिट्यूट. सर्व हक्क राखीव.",
    "Certified by Bharat Sevak Samaj · Dadar, Mumbai":
        "भारत सेवक समाज प्रमाणित · दादर, मुंबई",
    "Counselling hours are best confirmed by telephone before visiting. Parents and guardians are encouraged to attend.":
        "भेटीपूर्वी समुपदेशनाची वेळ फोनवरून निश्चित करावी. पालकांनी सोबत यावे अशी विनंती.",
    "Call +91 86919 73874": "फोन करा +91 86919 73874",
    "Admissions 2026–27": "प्रवेश २०२६–२७",
    "Patient Care": "पेशंट केअर",
    "Medical Lab Technology": "मेडिकल लॅब टेक्नॉलॉजी",
    "Operation Theatre": "ऑपरेशन थिएटर",
    "Optometry": "ऑप्टोमेट्री",
    "DMLT": "DMLT",
    "Months 1–5": "महिने १–५",
    "Months 6–10": "महिने ६–१०",
    "Months 11–15": "महिने ११–१५",
    "Months 16–20": "महिने १६–२०",
    "Please telephone before visiting to confirm counselling hours. Correspondence is by email and WhatsApp; important correspondence is sent by speed post.":
        "भेटीपूर्वी समुपदेशनाची वेळ फोनवरून निश्चित करा. पत्रव्यवहार ईमेल व व्हॉट्सअ‍ॅपद्वारे होतो; महत्त्वाचा पत्रव्यवहार स्पीडपोस्टने पाठवला जातो.",
})

# ---------------------------------------------------------------- hero / homepage
MR.update({
    "Train for a hospital job.": "हॉस्पिटलमधील नोकरीसाठी प्रशिक्षण घ्या.",
    "Earn while you train.": "शिकता शिकता कमवा.",
    "Admissions open · 2026–27 batch": "प्रवेश सुरू · २०२६–२७ बॅच",
    "Two-year paramedical diplomas in Dadar, certified by Bharat Sevak Samaj — a national development agency promoted by the Government of India since 1952. Full-time hospital and laboratory postings from the fifth month, with a monthly stipend that rises as you qualify.":
        "दादर येथे दोन वर्षांचे पॅरामेडिकल डिप्लोमा, भारत सेवक समाज प्रमाणित — ही १९५२ पासून भारत सरकारने पुरस्कृत केलेली राष्ट्रीय विकास संस्था आहे. पाचव्या महिन्यापासून हॉस्पिटल व प्रयोगशाळेत पूर्णवेळ पोस्टिंग, आणि पात्रता वाढेल तसा वाढणारा मासिक स्टायपेंड.",
    "Placement assistance covers private hospitals, clinics and diagnostic laboratories. It does not extend to Government hospital appointments. DPC & DPCA are not affiliated to the Indian Nursing Council.":
        "नोकरीचे सहाय्य खाजगी हॉस्पिटल, क्लिनिक व डायग्नोस्टिक प्रयोगशाळांपुरते आहे. सरकारी हॉस्पिटलमधील नियुक्तीची हमी नाही. DPC व DPCA यांचा इंडियन नर्सिंग कौन्सिलशी संबंध नाही.",
    "National Development Agency promoted by the Government of India. Founder President: Pandit Jawaharlal Nehru. Constitution approved unanimously by the Indian Parliament.":
        "भारत सरकारने पुरस्कृत केलेली राष्ट्रीय विकास संस्था. संस्थापक अध्यक्ष: पंडित जवाहरलाल नेहरू. घटना भारतीय संसदेने एकमताने मंजूर केली.",
    "Years": "वर्षे", "Students": "विद्यार्थी", "Stipendiary": "स्टायपेंडसह",
    "Teaching": "अध्यापन", "Placed": "नोकरी मिळाली", "Diplomas": "डिप्लोमा",
    "Months — classroom training followed by full-time hospital posting":
        "महिने — वर्गातील प्रशिक्षण, त्यानंतर पूर्णवेळ हॉस्पिटल पोस्टिंग",
    "Typical total stipend earned over the two-year diploma":
        "दोन वर्षांच्या डिप्लोमामध्ये मिळणारा एकूण स्टायपेंड",
    "10th / 12th": "१० वी / १२ वी",
    "Pass or fail — eligible to apply for the diploma courses":
        "पास किंवा नापास — डिप्लोमा कोर्सेससाठी अर्ज करू शकता",
    "Railway concession for students during classroom training":
        "वर्गातील प्रशिक्षणादरम्यान विद्यार्थ्यांना रेल्वे सवलत",
    "Government of India development agency, est. 1952": "भारत सरकार विकास संस्था, स्थापना १९५२",
    "Registered quality management system": "नोंदणीकृत गुणवत्ता व्यवस्थापन प्रणाली",
    "Accredited 2017–2027": "मान्यता २०१७–२०२७",
    "Authorised Skill Institute": "अधिकृत कौशल्य संस्था",
    "Four stipendiary diplomas": "स्टायपेंडसह चार डिप्लोमा",
    "Each runs four months of classroom training followed by twenty months of supervised posting in a Mumbai hospital, nursing home, laboratory or optician's practice.":
        "प्रत्येक कोर्समध्ये चार महिने वर्गातील प्रशिक्षण आणि नंतर मुंबईतील हॉस्पिटल, नर्सिंग होम, प्रयोगशाळा किंवा ऑप्टिशियनकडे वीस महिने देखरेखीखाली पोस्टिंग असते.",
    "One-year certificate courses": "एक वर्षाचे सर्टिफिकेट कोर्सेस",
    "Twelve programmes for in-service candidates with three or more years of experience. Study alongside your job; direct examination available for experienced candidates.":
        "तीन किंवा अधिक वर्षांचा अनुभव असलेल्या कार्यरत उमेदवारांसाठी बारा कोर्सेस. नोकरी सांभाळून शिका; अनुभवी उमेदवारांसाठी थेट परीक्षेची सोय.",
    "B.Voc & Advanced Diploma": "B.Voc व अ‍ॅडव्हान्स्ड डिप्लोमा",
    "Graduates of our two-year diplomas can enter a Bachelor of Vocation by lateral entry, or take the Advanced Diploma in Medical Laboratory Technology.":
        "आमचा दोन वर्षांचा डिप्लोमा पूर्ण केलेले विद्यार्थी लॅटरल एंट्रीने B.Voc मध्ये प्रवेश घेऊ शकतात, किंवा मेडिकल लॅबोरेटरी टेक्नॉलॉजीमधील अ‍ॅडव्हान्स्ड डिप्लोमा करू शकतात.",
    "Most of the fee comes back as stipend.": "बहुतांश फी स्टायपेंडमधून परत मिळते.",
    "Families rightly ask what a two-year diploma really costs. Here is the arithmetic in full, using the Diploma in Medical Laboratory Technology as the worked example — nothing withheld for a counselling call.":
        "दोन वर्षांच्या डिप्लोमाला प्रत्यक्षात किती खर्च येतो हा पालकांचा रास्त प्रश्न आहे. मेडिकल लॅबोरेटरी टेक्नॉलॉजी डिप्लोमाचे उदाहरण घेऊन संपूर्ण हिशोब येथे दिला आहे — समुपदेशनासाठी काहीही राखून ठेवलेले नाही.",
    "What you pay — D.M.L.T.": "तुम्ही किती भरता — डी.एम.एल.टी.",
    "Admission instalment": "प्रवेशाचा हप्ता",
    "First three monthly instalments": "पहिले तीन मासिक हप्ते",
    "Balance, staged to April 2028": "उर्वरित रक्कम, एप्रिल 2028 पर्यंत टप्प्याटप्प्याने",
    "Total course fee": "एकूण कोर्स फी",
    "What you earn back": "तुम्हाला किती परत मिळते",
    "Months 1–5 — ₹2,000/month": "महिने १–५ — ₹2,000/महिना",
    "Months 6–10 — ₹3,000/month": "महिने ६–१० — ₹3,000/महिना",
    "Months 11–15 — ₹4,000/month": "महिने ११–१५ — ₹4,000/महिना",
    "Months 16–20 — ₹5,000/month": "महिने १६–२० — ₹5,000/महिना",
    "Typical stipend earned": "साधारण मिळणारा स्टायपेंड",
    "Inclusive of textbooks, workbooks, notes, equipment, examination fee, registration and identity card.":
        "पाठ्यपुस्तके, कार्यपुस्तिका, नोट्स, साहित्य, परीक्षा फी, नोंदणी व ओळखपत्र यांचा समावेश.",
    "Paid by the nursing home, laboratory or clinic where you are posted, and may vary according to your work.":
        "ज्या नर्सिंग होम, प्रयोगशाळा किंवा क्लिनिकमध्ये पोस्टिंग असेल तेथून स्टायपेंड दिला जातो, आणि कामाप्रमाणे तो कमी-जास्त होऊ शकतो.",
    "The certification behind your diploma": "तुमच्या डिप्लोमामागील प्रमाणन",
    "A credential with a constitutional record.": "घटनात्मक नोंद असलेली मान्यता.",
    "Bharat Sevak Samaj is a national development agency promoted by the Government of India in 1952 to secure public co-operation in implementing government plans. Pandit Jawaharlal Nehru was its founder President, and its constitution and functioning were approved unanimously by the Indian Parliament.":
        "भारत सेवक समाज ही सरकारी योजनांच्या अंमलबजावणीत नागरिकांचे सहकार्य मिळवण्यासाठी भारत सरकारने १९५२ साली पुरस्कृत केलेली राष्ट्रीय विकास संस्था आहे. पंडित जवाहरलाल नेहरू हे तिचे संस्थापक अध्यक्ष होते, आणि तिची घटना व कार्यप्रणाली भारतीय संसदेने एकमताने मंजूर केली.",
    "Every diploma awarded at this institute is issued under that certification.":
        "या संस्थेत दिला जाणारा प्रत्येक डिप्लोमा याच प्रमाणनाखाली दिला जातो.",
    "How to join": "प्रवेश कसा घ्यावा",
    "Four steps from first enquiry to your first day of classroom training. Our counsellors confirm your eligibility before you pay anything.":
        "पहिल्या चौकशीपासून वर्गाच्या पहिल्या दिवसापर्यंत चार टप्पे. पैसे भरण्यापूर्वीच आमचे समुपदेशक तुमची पात्रता तपासतात.",
    "STEP 01": "टप्पा ०१", "STEP 02": "टप्पा ०२", "STEP 03": "टप्पा ०३", "STEP 04": "टप्पा ०४",
    "Enquire": "चौकशी करा", "Counselling": "समुपदेशन",
    "Submit documents": "कागदपत्रे जमा करा", "Confirm admission": "प्रवेश निश्चित करा",
    "Call or message us on WhatsApp with your name, the course you are considering, and your last examination result. We reply the same working day.":
        "तुमचे नाव, कोणता कोर्स करायचा आहे आणि शेवटच्या परीक्षेचा निकाल कळवून फोन करा किंवा व्हॉट्सअ‍ॅप करा. त्याच कामकाजाच्या दिवशी उत्तर मिळेल.",
    "Meet us at Dadar with a parent or guardian. We explain the course, the posting system and the full fee and stipend schedule before you commit.":
        "पालकांसह दादर येथे भेटा. कोर्स, पोस्टिंग पद्धत आणि संपूर्ण फी व स्टायपेंड वेळापत्रक प्रवेशापूर्वीच समजावून सांगितले जाते.",
    "Mark sheets, Aadhaar, leaving certificate, domicile, medical fitness certificate and photographs.":
        "गुणपत्रिका, आधार कार्ड, शाळा सोडल्याचा दाखला, अधिवास प्रमाणपत्र, वैद्यकीय तंदुरुस्ती प्रमाणपत्र व फोटो.",
    "Pay the first instalment to reserve your seat. Hospital posting follows in the fifth month.":
        "जागा राखून ठेवण्यासाठी पहिला हप्ता भरा. पाचव्या महिन्यापासून हॉस्पिटल पोस्टिंग सुरू होते.",
    "Letters from students who were placed": "नोकरी मिळालेल्या विद्यार्थ्यांची पत्रे",
    "Written by our own graduates after they found work, and reproduced as they wrote them. Three shown here span the range — a recent starter, a mid-career technician and a graduate of 2005. The English is a translation of the Marathi; the salary is the figure each writer states.":
        "नोकरी मिळाल्यानंतर आमच्याच विद्यार्थ्यांनी लिहिलेली पत्रे, जशीच्या तशी येथे दिली आहेत. येथील तीन पत्रे संपूर्ण श्रेणी दाखवतात — नुकतीच सुरुवात केलेली, मध्यम अनुभवाची आणि 2005 सालची विद्यार्थिनी. पगाराचा आकडा त्या-त्या विद्यार्थ्याने लिहिलेला आहे.",
    "Read all 14 letters": "सर्व 14 पत्रे वाचा",
    "Seats are limited, and the batch fills before September.":
        "जागा मर्यादित आहेत, आणि सप्टेंबरपूर्वीच बॅच भरते.",
    "Speak to a counsellor about which diploma fits your marks, your budget and the hospital you want to work in. Bring a parent or guardian — we would rather answer every question now than after you have paid.":
        "तुमचे गुण, बजेट आणि तुम्हाला ज्या हॉस्पिटलमध्ये काम करायचे आहे त्यानुसार कोणता डिप्लोमा योग्य आहे हे समुपदेशकाशी बोलून ठरवा. पालकांना सोबत आणा — फी भरल्यानंतर नव्हे तर आताच प्रत्येक प्रश्नाचे उत्तर देणे आम्हाला योग्य वाटते.",
})

# ---------------------------------------------------------------- about page
MR.update({
    "Three decades of training technicians for Mumbai's hospitals.":
        "मुंबईच्या हॉस्पिटलसाठी तीन दशके टेक्निशियन घडवत आहोत.",
    "We are a paramedical training institute in Dadar West. We teach four stipendiary diplomas, place our graduates in private hospitals, laboratories and clinics across the city, and certify them under Bharat Sevak Samaj.":
        "आम्ही दादर (प) येथील पॅरामेडिकल प्रशिक्षण संस्था आहोत. आम्ही स्टायपेंडसह चार डिप्लोमा शिकवतो, आमच्या विद्यार्थ्यांना शहरातील खाजगी हॉस्पिटल, प्रयोगशाळा व क्लिनिकमध्ये नोकरी मिळवून देतो, आणि भारत सेवक समाजाच्या मान्यतेने प्रमाणपत्र देतो.",
    "MBBS, DOMS, PhD. He founded the institute in 1996, wrote the manuals our students learn from, and still takes counselling visits himself.":
        "MBBS, DOMS, PhD. त्यांनी 1996 साली संस्थेची स्थापना केली, आमचे विद्यार्थी वापरतात ती पुस्तके लिहिली, आणि आजही ते स्वतः समुपदेशन भेटी घेतात.",
    "Who certifies what we teach": "आम्ही जे शिकवतो त्याला मान्यता कोणाची",
    "Bharat Sevak Samaj, ISO 9001:2015, HLACT International (2017–2027) and the World Skill Council. The certificates are reproduced in full.":
        "भारत सेवक समाज, ISO 9001:2015, HLACT International (2017–2027) व World Skill Council. सर्व प्रमाणपत्रे संपूर्ण दिली आहेत.",
    "An institute built around the posting, not the classroom.":
        "वर्गापेक्षा प्रत्यक्ष पोस्टिंगवर आधारलेली संस्था.",
    "Most paramedical courses in Mumbai teach theory and leave the student to find work afterwards. We built ours the other way round. Four months of classroom training establish the fundamentals; the remaining twenty months are spent on a full-time posting in a working nursing home, diagnostic laboratory, operation theatre or optician's practice, under a practising doctor.":
        "मुंबईतील बहुतेक पॅरामेडिकल कोर्सेस केवळ सिद्धांत शिकवतात आणि नंतर नोकरी शोधणे विद्यार्थ्यावर सोडतात. आम्ही याच्या उलट पद्धत निवडली. चार महिन्यांत वर्गातील प्रशिक्षणाने पाया पक्का होतो; उर्वरित वीस महिने प्रत्यक्ष चालू असलेल्या नर्सिंग होम, डायग्नोस्टिक प्रयोगशाळा, ऑपरेशन थिएटर किंवा ऑप्टिशियनकडे, प्रॅक्टिस करणाऱ्या डॉक्टरांच्या देखरेखीखाली पूर्णवेळ पोस्टिंगमध्ये जातात.",
    "That posting is where the diploma stops being theoretical. It is also where most of our placements originate — the laboratory or nursing home that trains a student for twenty months is very often the one that hires them.":
        "याच पोस्टिंगमध्ये डिप्लोमा पुस्तकी राहत नाही. आमच्या बहुतेक नोकऱ्या येथूनच मिळतात — जी प्रयोगशाळा किंवा नर्सिंग होम विद्यार्थ्याला वीस महिने प्रशिक्षण देते, तीच बहुतेक वेळा त्याला कामावर ठेवते.",
    "Founded in 1996, by a doctor": "1996 साली, एका डॉक्टरांनी स्थापन केली",
    "The institute was founded by": "संस्थेची स्थापना केली",
    "What we expect": "आमची अपेक्षा",
    "We are a strict institute, and we say so plainly. Ninety per cent attendance is compulsory. Uniforms are required on duty. Night duty is part of the Patient Care course, and laboratory students work two shifts. Students who cannot commit to this will not do well here, and we would rather say that at the counselling stage than after a fee has been paid.":
        "आम्ही शिस्तप्रिय संस्था आहोत, आणि हे आम्ही स्पष्ट सांगतो. नव्वद टक्के हजेरी अनिवार्य आहे. ड्युटीवर गणवेश आवश्यक आहे. पेशंट केअर कोर्समध्ये नाईट ड्युटी असते, आणि प्रयोगशाळेतील विद्यार्थ्यांना दोन शिफ्टमध्ये काम करावे लागते. ज्यांना हे जमणार नाही त्यांना येथे यश मिळणार नाही, आणि हे फी भरल्यानंतर सांगण्यापेक्षा समुपदेशनाच्या वेळीच सांगणे आम्हाला योग्य वाटते.",
    "What we do not claim": "आम्ही जे सांगत नाही",
    "Our placement assistance covers private hospitals, clinics and diagnostic laboratories. It does not extend to Government hospital appointments, and we will not suggest otherwise. The Diploma in Patient Care and Diploma in Patient Care Assistant have no affiliation with the Indian Nursing Council. Our certificate courses for working technicians carry neither stipend nor placement assistance.":
        "आमचे नोकरीचे सहाय्य खाजगी हॉस्पिटल, क्लिनिक व डायग्नोस्टिक प्रयोगशाळांपुरते आहे. सरकारी हॉस्पिटलमधील नियुक्तीची हमी आम्ही देत नाही, आणि तसे भासवतही नाही. डिप्लोमा इन पेशंट केअर व डिप्लोमा इन पेशंट केअर असिस्टंट यांचा इंडियन नर्सिंग कौन्सिलशी संबंध नाही. कार्यरत टेक्निशियनसाठीच्या आमच्या सर्टिफिकेट कोर्सेसना स्टायपेंड किंवा नोकरीचे सहाय्य नाही.",
    "Before you enrol": "प्रवेश घेण्यापूर्वी",
    "Ask us for the fee schedule, the refund rules and the posting terms in writing at your first visit. We give them to every family as a printed prospectus, and everything in it is also published on this website.":
        "पहिल्या भेटीतच फी वेळापत्रक, फी परतावा नियम आणि पोस्टिंगच्या अटी लेखी मागा. आम्ही प्रत्येक कुटुंबाला छापील प्रॉस्पेक्टस देतो, आणि त्यातील सर्व माहिती या वेबसाइटवरही प्रकाशित केलेली आहे.",
    "Virar–Kalyan–Chembur": "विरार–कल्याण–चेंबूर",
    "B.S.S. is a national development agency promoted by the Government of India in 1952 to secure public co-operation in implementing government plans. Pandit Jawaharlal Nehru was its founder President.":
        "भा.से.स. ही सरकारी योजनांच्या अंमलबजावणीत नागरिकांचे सहकार्य मिळवण्यासाठी भारत सरकारने १९५२ साली पुरस्कृत केलेली राष्ट्रीय विकास संस्था आहे. पंडित जवाहरलाल नेहरू हे तिचे संस्थापक अध्यक्ष होते.",
    "Its constitution and functioning were approved unanimously by the Indian Parliament — recorded in the First Five Year Plan, in the chapter on public co-operation in national development. Every diploma awarded at this institute is issued under that certification.":
        "तिची घटना व कार्यप्रणाली भारतीय संसदेने एकमताने मंजूर केली — याची नोंद पहिल्या पंचवार्षिक योजनेत, 'राष्ट्रीय विकासात नागरिकांचे सहकार्य' या प्रकरणात आहे. या संस्थेत दिला जाणारा प्रत्येक डिप्लोमा याच प्रमाणनाखाली दिला जातो.",
    "The certificate itself": "प्रमाणपत्र स्वतः",
    "What you are awarded": "तुम्हाला काय मिळते",
    "A specimen of the certificate issued on successful completion, carrying the Bharat Sevak Samaj seal, your register number, the course and year, and the division obtained in theory and practicals. It is signed by the Director and by the Chairman of the Board of Examinations.":
        "कोर्स यशस्वीपणे पूर्ण केल्यावर मिळणाऱ्या प्रमाणपत्राचा नमुना — त्यावर भारत सेवक समाजाचा शिक्का, तुमचा नोंदणी क्रमांक, कोर्स व वर्ष, आणि सिद्धांत व प्रात्यक्षिकातील श्रेणी असते. त्यावर संचालक व परीक्षा मंडळाचे अध्यक्ष यांची सही असते.",
    "Our students on posting": "पोस्टिंगवरील आमचे विद्यार्थी",
    "Photographs from the institute's own archive, taken at the nursing homes, laboratories and clinics where our students train.":
        "संस्थेच्या स्वतःच्या संग्रहातील छायाचित्रे — आमचे विद्यार्थी जेथे प्रशिक्षण घेतात त्या नर्सिंग होम, प्रयोगशाळा व क्लिनिकमध्ये काढलेली.",
    "Come and see the institute before you decide.": "ठरवण्यापूर्वी संस्थेला भेट द्या.",
    "We would rather you visit, meet the staff and ask difficult questions than enrol on the strength of a website. Telephone first to confirm counselling hours.":
        "केवळ वेबसाइट पाहून प्रवेश घेण्यापेक्षा तुम्ही प्रत्यक्ष यावे, कर्मचाऱ्यांना भेटावे आणि कठीण प्रश्न विचारावे असे आम्हाला वाटते. समुपदेशनाची वेळ आधी फोनवरून निश्चित करा.",
})

# ---------------------------------------------------------------- courses hub
MR.update({
    "Every course we teach, with the fee printed.": "आम्ही शिकवणारा प्रत्येक कोर्स, फीसह.",
    "Three tracks: two-year stipendiary diplomas for school leavers, one-year certificates for technicians already in service, and a degree pathway for diploma holders who want to go further.":
        "तीन गट: शाळा पूर्ण केलेल्यांसाठी स्टायपेंडसह दोन वर्षांचे डिप्लोमा, आधीच कार्यरत असलेल्या टेक्निशियनसाठी एक वर्षाचे सर्टिफिकेट, आणि पुढे शिकू इच्छिणाऱ्या डिप्लोमाधारकांसाठी पदवी मार्ग.",
    "Two-year stipendiary diplomas": "स्टायपेंडसह दोन वर्षांचे डिप्लोमा",
    "Four months of classroom training followed by twenty months of full-time supervised posting. These four courses carry a written stipend and placement assistance.":
        "चार महिने वर्गातील प्रशिक्षण आणि नंतर वीस महिने देखरेखीखाली पूर्णवेळ पोस्टिंग. या चार कोर्सेसना लेखी स्टायपेंड व नोकरीचे सहाय्य आहे.",
    "Placement assistance covers private hospitals, clinics and diagnostic laboratories only. DPC and DPCA have no affiliation with the Indian Nursing Council. The X-Ray Technician course is open to male candidates only.":
        "नोकरीचे सहाय्य केवळ खाजगी हॉस्पिटल, क्लिनिक व डायग्नोस्टिक प्रयोगशाळांपुरते आहे. DPC व DPCA यांचा इंडियन नर्सिंग कौन्सिलशी संबंध नाही. एक्स-रे टेक्निशियन कोर्स फक्त पुरुष उमेदवारांसाठी आहे.",
    "One-year certificates for working technicians": "कार्यरत टेक्निशियनसाठी एक वर्षाचे सर्टिफिकेट",
    "For candidates already in service with three or more years of experience. Study alongside your job. These courses are non-stipendiary and are not covered by placement assistance.":
        "तीन किंवा अधिक वर्षांचा अनुभव असलेल्या कार्यरत उमेदवारांसाठी. नोकरी सांभाळून शिका. या कोर्सेसना स्टायपेंड नाही व नोकरीचे सहाय्यही नाही.",
    "Diploma holders can continue to a Bachelor of Vocation by lateral entry, or take the Advanced Diploma in Medical Laboratory Technology.":
        "डिप्लोमाधारक लॅटरल एंट्रीने B.Voc करू शकतात, किंवा मेडिकल लॅबोरेटरी टेक्नॉलॉजीमधील अ‍ॅडव्हान्स्ड डिप्लोमा करू शकतात.",
    "3 years · 6 semesters": "३ वर्षे · ६ सत्रे",
    "2 years · 4 semesters": "२ वर्षे · ४ सत्रे",
    "B.Voc — regular entry": "B.Voc — नियमित प्रवेश",
    "B.Voc — lateral entry": "B.Voc — लॅटरल एंट्री",
    "Medical Lab Technology or Patient Care Management. Eligibility: 12th pass with 60% or above.":
        "मेडिकल लॅब टेक्नॉलॉजी किंवा पेशंट केअर मॅनेजमेंट. पात्रता: १२ वी ६०% किंवा अधिक गुणांसह उत्तीर्ण.",
    "For holders of a two-year BSS diploma. Enter directly in the third semester.":
        "दोन वर्षांचा बी.एस.एस. डिप्लोमा असलेल्यांसाठी. थेट तिसऱ्या सत्रात प्रवेश.",
    "Advanced Diploma (ADMLT)": "अ‍ॅडव्हान्स्ड डिप्लोमा (ADMLT)",
    "Advanced Diploma in Medical Laboratory Technology, after a BSS diploma.":
        "बी.एस.एस. डिप्लोमानंतर मेडिकल लॅबोरेटरी टेक्नॉलॉजीमधील अ‍ॅडव्हान्स्ड डिप्लोमा.",
    "Not sure which course fits?": "कोणता कोर्स योग्य आहे हे ठरत नाही?",
    "Tell a counsellor your last examination result and what you would like to do, and we will tell you honestly which of these courses you are eligible for.":
        "तुमच्या शेवटच्या परीक्षेचा निकाल आणि तुम्हाला काय करायचे आहे हे समुपदेशकाला सांगा, आणि यांपैकी कोणत्या कोर्ससाठी तुम्ही पात्र आहात हे आम्ही प्रामाणिकपणे सांगू.",
    "Diploma in Patient Care / Patient Care Assistant": "डिप्लोमा इन पेशंट केअर / पेशंट केअर असिस्टंट",
    "Diploma in Medical Laboratory Technology": "डिप्लोमा इन मेडिकल लॅबोरेटरी टेक्नॉलॉजी",
    "Diploma in Operation Theatre Technician": "डिप्लोमा इन ऑपरेशन थिएटर टेक्निशियन",
    "Diploma in Optometry": "डिप्लोमा इन ऑप्टोमेट्री",
    "B.Voc in Medical Lab Technology": "B.Voc इन मेडिकल लॅब टेक्नॉलॉजी",
    "B.Voc in Patient Care Management": "B.Voc इन पेशंट केअर मॅनेजमेंट",
    "REGULAR ENTRY": "नियमित प्रवेश", "LATERAL ENTRY": "लॅटरल एंट्री",
    "then 30 × ₹4,600": "नंतर 30 × ₹4,600", "then 20 × ₹4,000": "नंतर 20 × ₹4,000",
    "then 11 × ₹3,000": "नंतर 11 × ₹3,000",
})

# ---------------------------------------------------------------- course detail pages
MR.update({
    "What you will learn": "तुम्ही काय शिकाल",
    "How the two years run": "दोन वर्षे कशी चालतात",
    "Where graduates work": "विद्यार्थी कुठे काम करतात",
    "Please note": "कृपया लक्षात घ्या",
    "The fee, and what comes back": "फी, आणि किती परत मिळते",
    "Your monthly stipend rises as you qualify": "पात्रता वाढेल तसा मासिक स्टायपेंड वाढतो",
    "Other diplomas": "इतर डिप्लोमा",
    "Where this diploma led": "या डिप्लोमानंतर काय मिळाले",
    "Letters from students who took this course, reproduced as they wrote them. The salary is the figure each writer states, not a figure we promise.":
        "हा कोर्स केलेल्या विद्यार्थ्यांची पत्रे, जशीच्या तशी दिली आहेत. पगाराचा आकडा त्या-त्या विद्यार्थ्याने लिहिलेला आहे, आम्ही दिलेले वचन नाही.",
    "Message us with your last examination result and we will confirm your eligibility the same working day. Counselling is free, and we will show you the full fee and refund terms before you pay.":
        "शेवटच्या परीक्षेचा निकाल कळवा, त्याच कामकाजाच्या दिवशी तुमची पात्रता आम्ही निश्चित करू. समुपदेशन मोफत आहे, आणि फी भरण्यापूर्वी संपूर्ण फी व परतावा अटी दाखवल्या जातील.",
    "Stipend is paid by the host nursing home, laboratory or clinic and may vary above or below these figures according to your work. Uniform and apron are purchased by the student, and entry to duty is refused without them.":
        "स्टायपेंड संबंधित नर्सिंग होम, प्रयोगशाळा किंवा क्लिनिककडून दिला जातो आणि कामाप्रमाणे तो या आकड्यांपेक्षा कमी-जास्त होऊ शकतो. गणवेश व एप्रन विद्यार्थ्याने स्वखर्चाने घ्यावा; त्याशिवाय ड्युटीवर प्रवेश दिला जात नाही.",
    # DPC
    "Trains you to care for admitted patients in nursing homes and hospitals — vital signs, ward procedure, patient hygiene, mobility, and assisting nursing and medical staff on duty.":
        "नर्सिंग होम व हॉस्पिटलमध्ये दाखल रुग्णांची काळजी घेण्याचे प्रशिक्षण — महत्त्वाची लक्षणे नोंदवणे, वॉर्डातील कार्यपद्धती, रुग्णाची स्वच्छता, हालचाल, आणि ड्युटीवरील नर्सिंग व वैद्यकीय कर्मचाऱ्यांना मदत.",
    "Recording and charting vital signs — temperature, pulse, respiration, blood pressure":
        "महत्त्वाची लक्षणे नोंदवणे — तापमान, नाडी, श्वसन, रक्तदाब",
    "Bed-making, patient positioning, hygiene and pressure-sore prevention":
        "बेड तयार करणे, रुग्णाची स्थिती, स्वच्छता व जखमा टाळणे",
    "Assisting with feeding, mobility and personal care of admitted patients":
        "दाखल रुग्णांना जेवण, हालचाल व वैयक्तिक काळजीत मदत",
    "Ward procedure, infection control and handling of medical waste":
        "वॉर्डातील कार्यपद्धती, संसर्ग नियंत्रण व वैद्यकीय कचरा हाताळणी",
    "Basic first aid, oxygen administration and emergency response":
        "प्राथमिक उपचार, ऑक्सिजन देणे व आपत्कालीन प्रतिसाद",
    "Maintaining patient records and handing over between shifts":
        "रुग्णांच्या नोंदी ठेवणे व शिफ्ट बदलताना माहिती देणे",
    "Patient care assistant in a private nursing home or hospital":
        "खाजगी नर्सिंग होम किंवा हॉस्पिटलमध्ये पेशंट केअर असिस्टंट",
    "Ward assistant / ward attendant": "वॉर्ड असिस्टंट / वॉर्ड अटेंडंट",
    "Home-care attendant for post-operative patients": "शस्त्रक्रियेनंतरच्या रुग्णांसाठी घरगुती सेवक",
    "Assistant in a day-care or dialysis unit": "डे-केअर किंवा डायलिसिस युनिटमध्ये सहाय्यक",
    "Night duty is compulsory for this course. This diploma has no affiliation with the Indian Nursing Council, and does not qualify the holder as a registered nurse.":
        "या कोर्ससाठी नाईट ड्युटी अनिवार्य आहे. या डिप्लोमाचा इंडियन नर्सिंग कौन्सिलशी संबंध नाही, आणि यामुळे धारक नोंदणीकृत नर्स होत नाही.",
    "Patient Care graduates": "पेशंट केअर विद्यार्थी",
    "Apply for the Patient Care diploma.": "पेशंट केअर डिप्लोमासाठी अर्ज करा.",
    # DMLT
    "Trains you to run the routine tests a diagnostic laboratory depends on — haematology, biochemistry, microbiology and sample handling, on real equipment under a pathologist.":
        "डायग्नोस्टिक प्रयोगशाळेत लागणाऱ्या नेहमीच्या चाचण्या करण्याचे प्रशिक्षण — हिमॅटोलॉजी, बायोकेमिस्ट्री, मायक्रोबायोलॉजी व नमुना हाताळणी, पॅथॉलॉजिस्टच्या देखरेखीखाली प्रत्यक्ष उपकरणांवर.",
    "Blood collection (venepuncture), sample labelling, transport and storage":
        "रक्त संकलन (व्हेनिपंक्चर), नमुन्यावर लेबल लावणे, वाहतूक व साठवण",
    "Haematology — haemoglobin, cell counts, ESR, blood grouping and cross-matching":
        "हिमॅटोलॉजी — हिमोग्लोबिन, पेशी मोजणी, ESR, रक्तगट व क्रॉस-मॅचिंग",
    "Clinical biochemistry — blood sugar, lipid profile, liver and kidney function tests":
        "क्लिनिकल बायोकेमिस्ट्री — रक्तशर्करा, लिपिड प्रोफाइल, यकृत व मूत्रपिंड चाचण्या",
    "Microbiology — staining, culture technique, and basic identification":
        "मायक्रोबायोलॉजी — स्टेनिंग, कल्चर तंत्र व प्राथमिक ओळख",
    "Urine, stool and body-fluid analysis": "लघवी, शौच व शरीरद्रव यांचे विश्लेषण",
    "Laboratory safety, quality control, reagent preparation and equipment maintenance":
        "प्रयोगशाळेतील सुरक्षा, गुणवत्ता नियंत्रण, अभिकर्मक तयार करणे व उपकरण देखभाल",
    "Laboratory technician in a diagnostic centre or pathology laboratory":
        "डायग्नोस्टिक सेंटर किंवा पॅथॉलॉजी प्रयोगशाळेत लॅब टेक्निशियन",
    "Phlebotomist / sample collection technician": "फ्लेबोटोमिस्ट / नमुना संकलन टेक्निशियन",
    "Hospital laboratory assistant": "हॉस्पिटल प्रयोगशाळा सहाय्यक",
    "Blood bank technician (with the additional certificate)":
        "ब्लड बँक टेक्निशियन (अतिरिक्त प्रमाणपत्रासह)",
    "This is our most subscribed course, and requires 12th pass or fail. Students are expected to work in two shifts or on break duty during the posting.":
        "हा आमचा सर्वाधिक मागणी असलेला कोर्स असून त्यासाठी १२ वी पास किंवा नापास आवश्यक आहे. पोस्टिंगदरम्यान विद्यार्थ्यांनी दोन शिफ्टमध्ये किंवा ब्रेक ड्युटीवर काम करणे अपेक्षित आहे.",
    "Medical Lab Technology graduates": "मेडिकल लॅब टेक्नॉलॉजी विद्यार्थी",
    "Apply for the Medical Lab Technology diploma.": "मेडिकल लॅब टेक्नॉलॉजी डिप्लोमासाठी अर्ज करा.",
    # DOTT
    "Trains you to prepare and run an operation theatre — sterilisation, instrument handling, theatre discipline and assisting the surgical team during procedures.":
        "ऑपरेशन थिएटर तयार करणे व चालवणे याचे प्रशिक्षण — निर्जंतुकीकरण, उपकरणे हाताळणी, थिएटरमधील शिस्त, आणि शस्त्रक्रियेदरम्यान सर्जिकल टीमला मदत.",
    "Sterilisation technique, autoclaving and maintaining the sterile field":
        "निर्जंतुकीकरण तंत्र, ऑटोक्लेव्हिंग व निर्जंतुक क्षेत्र राखणे",
    "Identification, handling and counting of surgical instruments":
        "शस्त्रक्रिया उपकरणांची ओळख, हाताळणी व मोजणी",
    "Theatre preparation, positioning and draping of the patient":
        "थिएटरची तयारी, रुग्णाची स्थिती व ड्रेपिंग",
    "Assisting the surgeon and anaesthetist during procedures":
        "शस्त्रक्रियेदरम्यान सर्जन व भूलतज्ज्ञांना मदत",
    "Handling of specimens, sharps and biomedical waste":
        "नमुने, धारदार साहित्य व जैववैद्यकीय कचरा हाताळणी",
    "Post-operative theatre cleaning and turnaround":
        "शस्त्रक्रियेनंतर थिएटरची स्वच्छता व पुनर्तयारी",
    "Operation theatre technician in a private hospital or nursing home":
        "खाजगी हॉस्पिटल किंवा नर्सिंग होममध्ये ऑपरेशन थिएटर टेक्निशियन",
    "OT assistant in a day-surgery or maternity centre":
        "डे-सर्जरी किंवा प्रसूती केंद्रात ओटी असिस्टंट",
    "CSSD (sterile supply) technician": "सीएसएसडी (निर्जंतुक पुरवठा) टेक्निशियन",
    "Endoscopy or minor-procedure room assistant": "एंडोस्कोपी किंवा लहान शस्त्रक्रिया कक्ष सहाय्यक",
    "Requires the ability to stand for extended periods and to work at short notice when emergency procedures are scheduled.":
        "दीर्घकाळ उभे राहण्याची आणि आपत्कालीन शस्त्रक्रियेच्या वेळी तातडीने काम करण्याची तयारी आवश्यक आहे.",
    "Apply for the Operation Theatre diploma.": "ऑपरेशन थिएटर डिप्लोमासाठी अर्ज करा.",
    # DOPTO
    "Trains you to test vision and dispense spectacles — refraction, use of optical instruments, lens fitting and patient handling in an optician's practice or eye clinic.":
        "दृष्टी तपासणी व चष्मा देण्याचे प्रशिक्षण — रिफ्रॅक्शन, ऑप्टिकल उपकरणांचा वापर, लेन्स बसवणे, आणि ऑप्टिशियन किंवा नेत्र क्लिनिकमध्ये रुग्ण हाताळणी.",
    "Vision testing and refraction using trial lens sets and the retinoscope":
        "ट्रायल लेन्स सेट व रेटिनोस्कोप वापरून दृष्टी तपासणी व रिफ्रॅक्शन",
    "Use of the auto-refractometer, slit lamp and lensmeter":
        "ऑटो-रिफ्रॅक्टोमीटर, स्लिट लॅम्प व लेन्समीटरचा वापर",
    "Spectacle prescription reading, lens selection and frame fitting":
        "चष्म्याचे प्रिस्क्रिप्शन वाचणे, लेन्स निवड व फ्रेम बसवणे",
    "Contact lens basics, insertion, removal and hygiene counselling":
        "कॉन्टॅक्ट लेन्सची प्राथमिक माहिती, घालणे, काढणे व स्वच्छतेचे मार्गदर्शन",
    "Recognising common eye conditions for referral to an ophthalmologist":
        "नेत्रतज्ज्ञांकडे पाठवण्यासाठी सामान्य नेत्रविकार ओळखणे",
    "Shop practice — dispensing, edging, and patient follow-up":
        "दुकानातील कामकाज — चष्मा देणे, एजिंग व रुग्णाचा पाठपुरावा",
    "Optometrist assistant / refractionist in an optician's practice":
        "ऑप्टिशियनकडे ऑप्टोमेट्रिस्ट असिस्टंट / रिफ्रॅक्शनिस्ट",
    "Vision technician in an eye hospital or clinic": "नेत्र रुग्णालय किंवा क्लिनिकमध्ये व्हिजन टेक्निशियन",
    "Optical retail dispensing": "ऑप्टिकल किरकोळ विक्री",
    "Assistant in a community eye-screening programme": "सामुदायिक नेत्र तपासणी कार्यक्रमात सहाय्यक",
    "Apply for the Optometry diploma.": "ऑप्टोमेट्री डिप्लोमासाठी अर्ज करा.",
})

# ---------------------------------------------------------------- testimonials (originals)
# These 14 letters were written in Marathi; the English on the site is my
# translation. Here we restore the writers' own sense in Marathi.
MR.update({
    "I received my Gaikwad Institute certificate in 2005. My postings were with Dr. Parulekar (Jogeshwari) and Dr. Shah (Vile Parle). I now work at the Andheri maternity home (K East) and receive ₹50,000 a month.":
        "मला 2005 साली गायकवाड इन्स्टिट्यूटचे सर्टिफिकेट मिळाले होते. माझी पोस्टिंग डॉ. पारुळेकर (जोगेश्वरी) व डॉ. शाह (विलेपार्ले) यांच्याकडे होती. आता मी अंधेरी प्रसूतिगृह (के ईस्ट) येथे नोकरी करत आहे आणि मला ₹50,000 पगार मिळतो.",
    "I am a DPC student and received my certificate in 2008. I work at Hinduja Hospital and my monthly pay is ₹40,000 to ₹45,000. For this I am grateful to Dr. Gaikwad Institute.":
        "मी डी.पी.सी. ची विद्यार्थिनी आहे, मला 2008 मध्ये सर्टिफिकेट मिळाले आहे. मी हिंदुजा हॉस्पिटलमध्ये काम करते. मला दरमहिना ₹40,000 ते ₹45,000 पगार आहे. यासाठी मी डॉ. गायकवाड इन्स्टिट्यूटची आभारी आहे.",
    "My name is Sneha Santosh Mahajan. I am a DPC student and received my certificate in 2019. I now work at Hinduja Hospital and receive a salary of ₹25,000.":
        "माझे नाव स्नेहा संतोष महाजन आहे. मी डी.पी.सी. ची विद्यार्थिनी आहे, मला 2019 मध्ये सर्टिफिकेट मिळाले आहे. मी आता हिंदुजा हॉस्पिटलमध्ये जॉब करत आहे आणि मला ₹25,000 पगार मिळत आहे.",
    "I am a DMLT student and received my certificate in 2019. I now work at Panvel Mahanagar Palika (PMC) and my salary there is ₹20,000. I am very grateful to Dr. Gaikwad Institute.":
        "मी डी.एम.एल.टी. ची विद्यार्थिनी आहे, मला 2019 ला सर्टिफिकेट मिळाले आहे. मी आज पनवेल महानगरपालिका (PMC) मध्ये काम करत आहे. मला तेथे ₹20,000 पगार आहे. मी डॉ. गायकवाड इन्स्टिट्यूटची खूप खूप आभारी आहे.",
    "I am a DPC student and received my certificate in 2016. I now work at J.N.P.T. Hospital in Uran and my salary is ₹20,000.":
        "मी डी.पी.सी. ची विद्यार्थिनी आहे, मला 2016 मध्ये सर्टिफिकेट मिळाले आहे. मी आता J.N.P.T. हॉस्पिटल, उरण येथे नोकरी करत आहे. मला ₹20,000 पगार आहे.",
    "I did the DMLT course and received my certificate in 2017. I work at Thyrocare Lab on ₹18,000 a month, and also do two hours of blood collection at BMC for ₹250 a day.":
        "मी डी.एम.एल.टी. कोर्स केला आहे, मला 2017 मध्ये सर्टिफिकेट मिळाले. मी आता थायरोकेअर लॅबमध्ये जॉब करतो, मला ₹18,000 पगार मिळत आहे. मी बी.एम.सी. मध्ये पण 2 तासांसाठी ब्लड कलेक्शनचे काम करतो, तिथे मला प्रतिदिन ₹250 मिळतात.",
    "I am a DMLT student of Dr. Gaikwad Institute and received my certificate in 2015. I work at Shambhaji Nagar dispensary, Andheri (K East ward) and receive ₹18,000.":
        "मी डॉ. गायकवाड इन्स्टिट्यूटमध्ये डी.एम.एल.टी. ची विद्यार्थिनी आहे, मला 2015 साली सर्टिफिकेट मिळाले आहे. मी संभाजी नगर डिस्पेन्सरी, अंधेरी (के ईस्ट) येथे नोकरी करत आहे. मला तेथे ₹18,000 पगार मिळत आहे.",
    "I joined in 2016 and received my certificate in 2018. I now work at Wadia Hospital (Parel) and my salary there is ₹15,000. I am grateful to Dr. Gaikwad Institute.":
        "मी 2016 ची विद्यार्थिनी आहे, मला 2018 मध्ये सर्टिफिकेट मिळाले. मी आता वाडिया हॉस्पिटल (परळ) येथे जॉब करत आहे. मला तिथे ₹15,000 पगार आहे. मी डॉ. गायकवाड इन्स्टिट्यूटची आभारी आहे.",
    "I am a DMLT student, batch 15, on posting at Nanavati Hospital (Vile Parle). The institute wrote my stipend as ₹4,000, but after PF deduction I receive ₹14,000 there. My training is still continuing.":
        "मी डी.एम.एल.टी. ची विद्यार्थिनी आहे, माझा बॅच नं. 15 आहे. मी नानावटी हॉस्पिटल (विलेपार्ले) येथे प्रॅक्टिकलसाठी आहे. मला इन्स्टिट्यूटमधून स्टायपेंड ₹4,000 लिहून दिला होता, पण मला तिथे पी.एफ. कापून ₹14,000 मिळतात. माझी अजूनही ट्रेनिंग सुरू आहे.",
    "I am a DMLT student of the 2020–2021 batch and received my certificate in 2021. I now work on the J. J. Hospital campus (Sandhurst Road) and my salary is ₹12,000.":
        "मी डी.एम.एल.टी. ची विद्यार्थिनी आहे, माझा बॅच 2020–2021 चा आहे. मला 2021 मध्ये सर्टिफिकेट मिळाले आहे. मी आता जे.जे. हॉस्पिटल कॅम्पस (सँडहर्स्ट रोड) येथे जॉब करत आहे. मला ₹12,000 पगार आहे.",
    "I completed DMLT at Dr. Gaikwad Institute in 2021. I now work at (BDBA) Shatabdi Hospital, Kandivali, and receive ₹12,000. For this I am very grateful to the institute.":
        "मी डॉ. गायकवाड इन्स्टिट्यूटमधून 2021 मध्ये डी.एम.एल.टी. पूर्ण केले आहे. मी आज (BDBA) शताब्दी हॉस्पिटल (कांदिवली) येथे जॉब करत असून मला ₹12,000 रुपये पगार मिळत आहे. याबद्दल मी इन्स्टिट्यूटचा खूप आभारी आहे.",
    "I completed DMLT at Dr. Gaikwad Institute in 2021 and now work at (BDBA) Shatabdi Hospital, Kandivali, receiving a salary of ₹12,000.":
        "मी डॉ. गायकवाड इन्स्टिट्यूटमधून 2021 मध्ये डी.एम.एल.टी. पूर्ण केले आहे. मी आज (BDBA) शताब्दी हॉस्पिटल (कांदिवली) येथे जॉब करत असून मला ₹12,000 रुपये पगार मिळत आहे.",
    "I am a DMLT student and received my certificate in 2016. I now have a job at K.E.M. (Parel) Hospital where my salary is ₹11,000.":
        "मी डी.एम.एल.टी. ची विद्यार्थिनी आहे, मला सर्टिफिकेट 2016 मध्ये मिळाले आहे. मी आता के.ई.एम. (परळ) हॉस्पिटल येथे जॉब करत आहे, तेथे मला ₹11,000 पगार आहे.",
    "I completed the D.M.L.T. course of 2021–2023 at Dr. Gaikwad Institute. After completing it I got an excellent opportunity to work at Nair Hospital, with a starting salary of ₹10,000.":
        "मी डॉ. गायकवाड इन्स्टिट्यूटमधून डी.एम.एल.टी. कोर्स 2021–2023 या साली पूर्ण केला. हा कोर्स पूर्ण झाल्यानंतर मला नायर हॉस्पिटल येथे जॉब करण्याची उत्तम संधी मिळाली. माझा स्टार्टिंग सॅलरी ₹10,000 आहे.",
})

# ---------------------------------------------------------------- certificates / bvoc / fees / refund
MR.update({
    "One-year certificates for technicians already in service.": "आधीच कार्यरत असलेल्या टेक्निशियनसाठी एक वर्षाचे सर्टिफिकेट.",
    "Twelve programmes for candidates with three or more years of work experience who want a formal qualification without leaving their job. Direct examination is available for experienced candidates.":
        "नोकरी न सोडता औपचारिक पात्रता मिळवू इच्छिणाऱ्या, तीन किंवा अधिक वर्षांचा अनुभव असलेल्या उमेदवारांसाठी बारा कोर्सेस. अनुभवी उमेदवारांसाठी थेट परीक्षेची सोय आहे.",
    "Before you read further": "पुढे वाचण्यापूर्वी",
    "These courses are": "हे कोर्सेस",
    "non-stipendiary": "स्टायपेंडविरहित आहेत",
    "not covered by placement assistance": "नोकरीच्या सहाय्यात समाविष्ट नाहीत",
    "two-year diploma courses": "दोन वर्षांचे डिप्लोमा कोर्सेस",
    "Three years in service": "तीन वर्षांचा अनुभव",
    "All twelve courses are for in-service candidates with a minimum of three years of relevant work experience. Bring evidence of employment to your counselling visit.":
        "हे बारा कोर्सेस किमान तीन वर्षांचा संबंधित अनुभव असलेल्या कार्यरत उमेदवारांसाठी आहेत. समुपदेशन भेटीच्या वेळी नोकरीचा पुरावा सोबत आणा.",
    "Study alongside your job": "नोकरी सांभाळून शिका",
    "Teaching is arranged so that working technicians can attend without leaving employment. Direct examination is available for suitably experienced candidates.":
        "कार्यरत टेक्निशियनना नोकरी न सोडता उपस्थित राहता यावे अशा प्रकारे अध्यापनाची रचना आहे. योग्य अनुभव असलेल्या उमेदवारांसाठी थेट परीक्षेची सोय आहे.",
    "Already working, and want the qualification on paper?": "आधीच कार्यरत आहात आणि कागदोपत्री पात्रता हवी आहे?",
    "Tell us your current role and how long you have been in it, and we will confirm which of the twelve certificates you are eligible for.":
        "तुमचे सध्याचे काम आणि किती काळापासून करत आहात हे सांगा, आणि बारांपैकी कोणत्या सर्टिफिकेटसाठी तुम्ही पात्र आहात हे आम्ही निश्चित करू.",
    "From diploma to degree.": "डिप्लोमापासून पदवीपर्यंत.",
    "A Bachelor of Vocation under the UGC B.Voc scheme, offered in association with Shri Venkateshwara University. Holders of our two-year diploma enter laterally and finish the degree in two years instead of three.":
        "UGC च्या B.Voc योजनेअंतर्गत बॅचलर ऑफ व्होकेशन, श्री वेंकटेश्वरा विद्यापीठाच्या सहकार्याने. आमचा दोन वर्षांचा डिप्लोमा असलेले विद्यार्थी लॅटरल एंट्रीने प्रवेश घेऊन तीनऐवजी दोन वर्षांत पदवी पूर्ण करतात.",
    "Regular entry": "नियमित प्रवेश", "Lateral entry": "लॅटरल एंट्री",
    "Advanced Diploma": "अ‍ॅडव्हान्स्ड डिप्लोमा",
    "Bachelor of Vocation (B.Voc)": "बॅचलर ऑफ व्होकेशन (B.Voc)",
    "The UGC Bachelor of Vocation scheme is a skills-based undergraduate degree with multiple entry and exit points, mapped to industry job roles under the National Skills Qualification Framework.":
        "UGC ची बॅचलर ऑफ व्होकेशन योजना ही कौशल्याधारित पदवी असून तिला अनेक प्रवेश व निर्गम बिंदू आहेत, आणि ती राष्ट्रीय कौशल्य पात्रता आराखड्यानुसार उद्योगातील नोकऱ्यांशी जोडलेली आहे.",
    "Advanced Diploma in Medical Laboratory Technology": "अ‍ॅडव्हान्स्ड डिप्लोमा इन मेडिकल लॅबोरेटरी टेक्नॉलॉजी",
    "Two years saved, and ₹58,000": "दोन वर्षे आणि ₹58,000 यांची बचत",
    "A student who completes our two-year DMLT diploma and then enters the B.Voc laterally pays ₹92,000 for the degree instead of ₹1,50,000, and finishes in two years instead of three — while having earned a stipend throughout the diploma.":
        "आमचा दोन वर्षांचा डी.एम.एल.टी. डिप्लोमा पूर्ण करून लॅटरल एंट्रीने B.Voc मध्ये जाणारा विद्यार्थी पदवीसाठी ₹1,50,000 ऐवजी ₹92,000 भरतो, आणि तीनऐवजी दोन वर्षांत पदवी पूर्ण करतो — तेही डिप्लोमाच्या संपूर्ण काळात स्टायपेंड मिळवत.",
    "Students who have passed 12th in the Science stream are advised to consider B.Voc or the Advanced Diploma directly. Speak to a counsellor about which is the better fit for your marks and your intended career.":
        "१२ वी विज्ञान शाखेतून उत्तीर्ण झालेल्या विद्यार्थ्यांनी थेट B.Voc किंवा अ‍ॅडव्हान्स्ड डिप्लोमाचा विचार करावा. तुमच्या गुणांनुसार व करिअरनुसार कोणते योग्य आहे हे समुपदेशकाशी बोलून ठरवा.",
    "Offered in association with Shri Venkateshwara University under the UGC Bachelor of Vocation scheme. Confirm current affiliation status and approvals with the institute at your counselling visit.":
        "UGC च्या बॅचलर ऑफ व्होकेशन योजनेअंतर्गत श्री वेंकटेश्वरा विद्यापीठाच्या सहकार्याने. सध्याची संलग्नता व मान्यता समुपदेशन भेटीच्या वेळी संस्थेकडून निश्चित करून घ्या.",
    "Ask about the degree pathway.": "पदवी मार्गाविषयी विचारा.",
    "Whether B.Voc, ADMLT or a two-year diploma first is the better route depends on your marks and how soon you need to be earning. A counsellor will walk you through both.":
        "B.Voc, ADMLT की आधी दोन वर्षांचा डिप्लोमा — हे तुमचे गुण आणि तुम्हाला किती लवकर कमवायला सुरुवात करायची आहे यावर अवलंबून आहे. समुपदेशक दोन्ही पर्याय समजावून सांगतील.",
    "The whole fee schedule, published.": "संपूर्ण फी वेळापत्रक, प्रसिद्ध केलेले.",
    "Every fee we charge, every instalment date, the stipend you can expect against it, and the refund terms if you leave. Nothing is held back for a counselling call.":
        "आम्ही आकारत असलेली प्रत्येक फी, प्रत्येक हप्त्याची तारीख, त्यासमोर मिळणारा स्टायपेंड, आणि सोडल्यास परताव्याच्या अटी. समुपदेशनासाठी काहीही राखून ठेवलेले नाही.",
    "Worked in full for the Diploma in Medical Laboratory Technology, our highest-fee course. The other diplomas follow the same pattern at a lower fee.":
        "आमचा सर्वाधिक फी असलेला कोर्स — मेडिकल लॅबोरेटरी टेक्नॉलॉजी डिप्लोमा — याचा संपूर्ण हिशोब. इतर डिप्लोमा हीच पद्धत कमी फीमध्ये पाळतात.",
    "Inclusive of textbooks, workbooks, notes, equipment, examination fee, registration, identity card and record note fees.":
        "पाठ्यपुस्तके, कार्यपुस्तिका, नोट्स, साहित्य, परीक्षा फी, नोंदणी, ओळखपत्र व रेकॉर्ड नोट फी यांचा समावेश.",
    "Paid by the host nursing home, laboratory or clinic, and may vary according to your work.":
        "संबंधित नर्सिंग होम, प्रयोगशाळा किंवा क्लिनिककडून दिला जातो, आणि कामाप्रमाणे कमी-जास्त होऊ शकतो.",
    "Fee schedule — two-year diplomas": "फी वेळापत्रक — दोन वर्षांचे डिप्लोमा",
    "When each stage falls due": "प्रत्येक टप्प्याची अंतिम तारीख",
    "For the current admission cycle. Confirm the dates applicable to your batch at admission.":
        "सध्याच्या प्रवेश वर्षासाठी. तुमच्या बॅचला लागू तारखा प्रवेशाच्या वेळी निश्चित करून घ्या.",
    "The first instalment is payable in cash. Once your posting begins, the monthly instalment is deducted from your stipend and remitted to the institute directly by the doctor. Instalments are due before the 10th of each month; a 10% penalty applies to late instalments, and a student two instalments in arrears may not attend class. Convocation fee of ₹1,000 is payable in April 2028.":
        "पहिला हप्ता रोखीने भरावा लागतो. पोस्टिंग सुरू झाल्यावर मासिक हप्ता स्टायपेंडमधून वजा करून डॉक्टर थेट संस्थेला पाठवतात. हप्ते दर महिन्याच्या 10 तारखेपूर्वी भरावेत; उशिरा भरल्यास 10% दंड लागतो, आणि दोन हप्ते थकल्यास विद्यार्थ्याला वर्गात बसू दिले जात नाही. पदवीदान फी ₹1,000 एप्रिल 2028 मध्ये भरावी.",
    "One year, for working technicians": "एक वर्ष, कार्यरत टेक्निशियनसाठी",
    "All twelve certificate courses": "सर्व बारा सर्टिफिकेट कोर्सेस",
    "Then eight monthly instalments": "नंतर आठ मासिक हप्ते",
    "ADMLT — 1 year": "ADMLT — १ वर्ष",
    "What you do not pay extra for": "कशासाठी वेगळे पैसे लागत नाहीत",
    "Text books, notes, workbooks and equipment.": "पाठ्यपुस्तके, नोट्स, कार्यपुस्तिका व साहित्य.",
    "Examination & registration": "परीक्षा व नोंदणी",
    "Registration, examination, record note and identity card fees.": "नोंदणी, परीक्षा, रेकॉर्ड नोट व ओळखपत्र फी.",
    "Computer & English": "संगणक व इंग्रजी",
    "Computer course and English speaking course as per syllabus (courses 1–4).":
        "अभ्यासक्रमानुसार संगणक कोर्स व इंग्रजी संभाषण कोर्स (कोर्स १–४).",
    "Sports day, Ganeshotsav, Republic Day, cultural events and competitions.":
        "क्रीडा दिन, गणेशोत्सव, प्रजासत्ताक दिन, सांस्कृतिक कार्यक्रम व स्पर्धा.",
    "Not included: uniform and apron, which are purchased by the student and are compulsory for duty; and the ₹2,000 examination and certificate fee for the supplementary DGI certificates awarded in the final year.":
        "समाविष्ट नाही: गणवेश व एप्रन, जे विद्यार्थ्याने स्वखर्चाने घ्यायचे असून ड्युटीसाठी अनिवार्य आहेत; आणि शेवटच्या वर्षी दिल्या जाणाऱ्या अतिरिक्त DGI प्रमाणपत्रांची ₹2,000 परीक्षा व प्रमाणपत्र फी.",
    "The other side of the arithmetic": "हिशोबाची दुसरी बाजू",
    "What graduates go on to earn": "विद्यार्थी पुढे किती कमावतात",
    "Salaries are as reported by each graduate and are not a guarantee of earnings.":
        "पगाराचे आकडे त्या-त्या विद्यार्थ्याने सांगितलेले आहेत; कमाईची हमी नाही.",
    "Want this in writing before you decide?": "ठरवण्यापूर्वी हे लेखी हवे आहे?",
    "Ask us for the printed prospectus. It carries the same fee schedule, instalment dates and refund rules published on this page, and it is the binding record.":
        "आमच्याकडून छापील प्रॉस्पेक्टस मागा. या पानावर दिलेले तेच फी वेळापत्रक, हप्त्यांच्या तारखा व परतावा नियम त्यात आहेत, आणि तोच बंधनकारक दस्तऐवज आहे.",
    "Our refund terms are strict, and we publish them so that no family is surprised by them later. Read this page before you pay the first instalment.":
        "आमच्या परताव्याच्या अटी कडक आहेत, आणि नंतर कोणत्याही कुटुंबाला धक्का बसू नये म्हणून त्या आम्ही प्रसिद्ध करतो. पहिला हप्ता भरण्यापूर्वी हे पान वाचा.",
    "The two rules that matter most": "सर्वात महत्त्वाचे दोन नियम",
    "Withdrawal before": "प्रवेश रद्द केल्यास —",
    "Within 7 days of": "७ दिवसांच्या आत",
    "Within 1 month of": "१ महिन्याच्या आत",
    "Patient Care / Patient Care Assistant": "पेशंट केअर / पेशंट केअर असिस्टंट",
    "Operation Theatre / X-Ray / Optometry": "ऑपरेशन थिएटर / एक्स-रे / ऑप्टोमेट्री",
    "All other courses": "इतर सर्व कोर्सेस",
    "Figures shown are the amount": "दाखवलेली रक्कम म्हणजे",
    "deducted": "कापली जाणारी रक्कम",
    "How to claim a refund": "फी परतावा कसा मागावा",
    "Submit a written application to the institute.": "संस्थेकडे लेखी अर्ज द्यावा.",
    "State clearly the name in whose favour the cheque should be drawn.":
        "चेक कोणाच्या नावाने हवा आहे ते स्पष्ट लिहावे.",
    "The cheque is issued fifteen days after the application is received.":
        "अर्ज मिळाल्यानंतर पंधरा दिवसांनी चेक दिला जातो.",
    "All refunds are made by cheque only, sent by speed post at the student's cost.":
        "सर्व परतावे फक्त चेकद्वारे, स्पीडपोस्टने पाठवले जातात; त्याचा खर्च विद्यार्थ्याचा असतो.",
    "Related charges": "संबंधित शुल्क",
    "5% deducted": "५% कापले", "10% deducted": "१०% कापले", "25% deducted": "२५% कापले",
    "Commandant, Home Guards": "कमांडंट, होमगार्ड",
    "See the certificate →": "प्रमाणपत्र पहा →",
})

# ---------------------------------------------------------------- admissions page
MR.update({
    "How to join the institute.": "संस्थेत प्रवेश कसा घ्यावा.",
    "Four steps, one document checklist, and a set of rules we ask you to read before you sign rather than after. Counselling is free and carries no obligation.":
        "चार टप्पे, कागदपत्रांची एक यादी, आणि सही करण्यापूर्वीच वाचावेत असे नियम. समुपदेशन मोफत आहे व त्याचे कोणतेही बंधन नाही.",
    "Same day": "त्याच दिवशी", "Enquiry response": "चौकशीला उत्तर",
    "25 Sept": "२५ सप्टें", "Attendance required": "आवश्यक हजेरी",
    "Four steps to admission": "प्रवेशाचे चार टप्पे",
    "Call or message us on WhatsApp with your name, the course you are considering, and your last examination result. We reply the same working day and tell you honestly whether you are eligible.":
        "तुमचे नाव, कोणता कोर्स करायचा आहे आणि शेवटच्या परीक्षेचा निकाल कळवून फोन करा किंवा व्हॉट्सअ‍ॅप करा. त्याच कामकाजाच्या दिवशी उत्तर देऊन तुम्ही पात्र आहात की नाही हे प्रामाणिकपणे सांगू.",
    "Meet us at Dadar with a parent or guardian. We explain the course, the posting system, the full fee and stipend schedule and the refund terms, and answer every question before you commit.":
        "पालकांसह दादर येथे भेटा. कोर्स, पोस्टिंग पद्धत, संपूर्ण फी व स्टायपेंड वेळापत्रक आणि परताव्याच्या अटी समजावून सांगितल्या जातात, आणि प्रवेशापूर्वीच प्रत्येक प्रश्नाचे उत्तर दिले जाते.",
    "Bring the checklist below. Photographs must be in white uniform or dress against a white background.":
        "खालील यादीतील कागदपत्रे आणा. फोटो पांढऱ्या गणवेशात किंवा पांढऱ्या पोशाखात, पांढऱ्या पार्श्वभूमीवर असावेत.",
    "Pay the first instalment in cash to reserve your seat. Classroom training begins with your batch, and hospital posting follows in the fifth month.":
        "जागा राखून ठेवण्यासाठी पहिला हप्ता रोखीने भरा. तुमच्या बॅचसोबत वर्ग सुरू होतो, आणि पाचव्या महिन्यापासून हॉस्पिटल पोस्टिंग सुरू होते.",
    "Documents required at admission": "प्रवेशासाठी आवश्यक कागदपत्रे",
    "10th / 12th mark sheet (photocopy)": "१० वी / १२ वी गुणपत्रिका (छायाप्रत)",
    "Aadhaar card (photocopy)": "आधार कार्ड (छायाप्रत)",
    "Marriage certificate, if applicable (photocopy)": "विवाह प्रमाणपत्र, लागू असल्यास (छायाप्रत)",
    "Caste certificate, if applicable (photocopy)": "जात प्रमाणपत्र, लागू असल्यास (छायाप्रत)",
    "School / college leaving certificate": "शाळा / महाविद्यालय सोडल्याचा दाखला",
    "Domicile certificate": "अधिवास प्रमाणपत्र",
    "Medical fitness certificate": "वैद्यकीय तंदुरुस्ती प्रमाणपत्र",
    "Colour photographs — white dress, white background": "रंगीत फोटो — पांढरा पोशाख, पांढरी पार्श्वभूमी",
    "Parents' signature on the admission form is not compulsory for students above 18 years, though we strongly encourage a parent or guardian to attend the counselling visit regardless.":
        "१८ वर्षांवरील विद्यार्थ्यांसाठी प्रवेश अर्जावर पालकांची सही अनिवार्य नाही, तरीही समुपदेशन भेटीला पालकांनी सोबत यावे अशी आमची आग्रहाची विनंती आहे.",
    "Admission cycle": "प्रवेश वर्ष", "June–July": "जून–जुलै",
    "25 September": "२५ सप्टेंबर", "Month 5": "पाचवा महिना", "Aug / Sept": "ऑगस्ट / सप्टेंबर",
    "See the fee schedule": "फी वेळापत्रक पहा",
    "The rules you are agreeing to": "तुम्ही मान्य करत असलेले नियम",
    "We are a strict institute and we would rather you knew that now. These are the terms every student and parent signs at admission, summarised.":
        "आम्ही शिस्तप्रिय संस्था आहोत आणि हे तुम्हाला आताच माहीत असावे असे आम्हाला वाटते. प्रवेशाच्या वेळी प्रत्येक विद्यार्थी व पालक ज्या अटींवर सही करतात, त्यांचा हा सारांश.",
    "What attendance is required?": "किती हजेरी आवश्यक आहे?",
    "Ninety per cent attendance is compulsory. Absence due to illness must be notified to the institute in writing. A student absent for more than eight days may be given a repeat, particularly where examination marks are poor.":
        "नव्वद टक्के हजेरी अनिवार्य आहे. आजारपणामुळे गैरहजर राहिल्यास संस्थेला लेखी कळवणे आवश्यक आहे. आठ दिवसांपेक्षा जास्त गैरहजर राहिल्यास, विशेषतः परीक्षेत कमी गुण मिळाल्यास, विद्यार्थ्याला रिपीट दिली जाऊ शकते.",
    "What are the dress and conduct rules?": "पोशाख व वर्तनाचे नियम काय आहेत?",
    "Indecent clothing, sleeveless tops, T-shirts, make-up, jewellery and excessive cash are not permitted. Uniform and apron are compulsory on duty and entry is refused without them. Mobile phones must be kept on vibrate in class and on posting — a ₹500 fine applies on first use, and confiscation on the second.":
        "असभ्य कपडे, स्लीव्हलेस, टी-शर्ट, मेकअप, दागिने व जास्त रोकड आणण्यास मनाई आहे. ड्युटीवर गणवेश व एप्रन अनिवार्य असून त्याशिवाय प्रवेश दिला जात नाही. वर्गात व पोस्टिंगमध्ये मोबाईल व्हायब्रेट मोडवर ठेवावा — पहिल्यांदा वापरल्यास ₹500 दंड, दुसऱ्यांदा मोबाईल जप्त केला जातो.",
    "How are postings allocated?": "पोस्टिंग कशी दिली जाते?",
    "We try to place you near your residence, and postings are available up to Virar, Kalyan and Chembur — but not in Navi Mumbai or beyond. You may arrange your own posting, for which a request letter is issued one month in advance; if you do, the institute is not responsible for the teaching or stipend at that posting. Once a posting has been allocated by the institute, changing to one of your own attracts a ₹5,000 posting fee.":
        "शक्यतो घराजवळ पोस्टिंग देण्याचा प्रयत्न केला जातो; विरार, कल्याण व चेंबूरपर्यंत पोस्टिंग मिळू शकते — नवी मुंबई व त्यापलीकडे नाही. तुम्ही स्वतःहून पोस्टिंग आणू शकता, त्यासाठी एक महिना आधी विनंती पत्र दिले जाते; तसे केल्यास त्या पोस्टिंगमधील शिकवणी व स्टायपेंडसाठी संस्था जबाबदार राहणार नाही. संस्थेकडून पोस्टिंग मिळाल्यानंतर स्वतःहून पोस्टिंग बदलल्यास ₹5,000 पोस्टिंग फी आकारली जाते.",
    "What happens if there is a problem on posting?": "पोस्टिंगमध्ये अडचण आल्यास काय?",
    "Report it to the institute by email immediately and we will act on it; you will receive a reply by email. Leaving a posting without informing us in writing is treated as the student's fault and attracts a ₹5,000 posting fee before a new posting is allocated.":
        "तत्काळ ईमेलद्वारे संस्थेला कळवा, आम्ही कारवाई करू; उत्तर ईमेलनेच दिले जाईल. लेखी न कळवता पोस्टिंग सोडल्यास ती विद्यार्थ्याची चूक मानली जाते आणि नवीन पोस्टिंग देण्यापूर्वी ₹5,000 पोस्टिंग फी आकारली जाते.",
    "Who may contact the institute about a student?": "विद्यार्थ्याबाबत संस्थेशी कोण संपर्क करू शकते?",
    "Only the parent or guardian who signed the admission form. Contact by any other person attracts a ₹1,000 fine on the first occasion and ₹3,000 on the second. Please make appointments by email and bring your daily diary.":
        "फक्त प्रवेश अर्जावर सही केलेले पालक. इतर कोणी संपर्क केल्यास पहिल्यांदा ₹1,000 व दुसऱ्यांदा ₹3,000 दंड आकारला जातो. कृपया ईमेलद्वारे अपॉइंटमेंट घ्या आणि डेली डायरी सोबत आणा.",
    "What are fines used for?": "दंडाची रक्कम कशासाठी वापरली जाते?",
    "Fine collections are not used by the institute for itself. They fund student activities — snacks, saree day, colour day, Ganeshotsav, Dassehra, Diwali, New Year, sports day, Republic Day and competitions.":
        "दंडाची रक्कम संस्था स्वतःसाठी वापरत नाही. ती विद्यार्थ्यांच्या उपक्रमांसाठी वापरली जाते — अल्पोपहार, साडी डे, कलर डे, गणेशोत्सव, दसरा, दिवाळी, नवीन वर्ष, क्रीडा दिन, प्रजासत्ताक दिन व स्पर्धा.",
    "Can I take another course at the same time?": "मी एकाच वेळी दुसरा कोर्स करू शकतो का?",
    "Only with written permission from the institute, obtained in advance.":
        "फक्त संस्थेची आगाऊ लेखी परवानगी घेऊनच.",
    "When do I collect my certificate?": "प्रमाणपत्र कधी घ्यावे?",
    "Within one month of convocation. After that the institute is not responsible for damage to the certificate, and a late fee of ₹500 per year applies.":
        "पदवीदान समारंभानंतर एका महिन्याच्या आत. त्यानंतर प्रमाणपत्राच्या नुकसानीस संस्था जबाबदार राहणार नाही, आणि प्रति वर्ष ₹500 विलंब शुल्क लागेल.",
    "Ready to start your enquiry?": "चौकशी सुरू करायची आहे?",
    "Message us with your last examination result and the course you are considering. We will confirm your eligibility and arrange a counselling appointment.":
        "शेवटच्या परीक्षेचा निकाल आणि कोणता कोर्स करायचा आहे ते कळवा. आम्ही तुमची पात्रता निश्चित करून समुपदेशनाची वेळ ठरवू.",
})

# ---------------------------------------------------------------- placements page
MR.update({
    "Trained on the floor, not only in the classroom.": "फक्त वर्गात नव्हे, प्रत्यक्ष कामावर प्रशिक्षण.",
    "From the fifth month, students work full shifts under practising doctors in real nursing homes, laboratories and operation theatres. It is where the diploma stops being theoretical — and where most of our placements originate.":
        "पाचव्या महिन्यापासून विद्यार्थी प्रत्यक्ष नर्सिंग होम, प्रयोगशाळा व ऑपरेशन थिएटरमध्ये प्रॅक्टिस करणाऱ्या डॉक्टरांच्या देखरेखीखाली पूर्ण शिफ्ट काम करतात. येथेच डिप्लोमा पुस्तकी राहत नाही — आणि आमच्या बहुतेक नोकऱ्या येथूनच मिळतात.",
    "Twenty months inside a working practice": "प्रत्यक्ष चालू असलेल्या ठिकाणी वीस महिने",
    "The posting is not an observership. Students work full duty — two shifts or break duty for laboratory students, night duty for patient care students — under the supervision of the doctor running the practice.":
        "पोस्टिंग म्हणजे केवळ निरीक्षण नव्हे. विद्यार्थी पूर्ण ड्युटी करतात — प्रयोगशाळेतील विद्यार्थ्यांना दोन शिफ्ट किंवा ब्रेक ड्युटी, पेशंट केअरच्या विद्यार्थ्यांना नाईट ड्युटी — तेथील डॉक्टरांच्या देखरेखीखाली.",
    "Nursing homes, diagnostic laboratories, clinics and opticians. We place you as near your residence as we can, up to Virar, Kalyan and Chembur. Postings are not available in Navi Mumbai or beyond.":
        "नर्सिंग होम, डायग्नोस्टिक प्रयोगशाळा, क्लिनिक व ऑप्टिशियन. शक्य तितके घराजवळ पोस्टिंग दिले जाते, विरार, कल्याण व चेंबूरपर्यंत. नवी मुंबई व त्यापलीकडे पोस्टिंग मिळत नाही.",
    "Under a practising doctor": "प्रॅक्टिस करणाऱ्या डॉक्टरांच्या देखरेखीखाली",
    "Parents are welcome to visit the posting with the student after 8:00 pm. We advise against a posting more than forty minutes' walk from the station.":
        "पालकांनी विद्यार्थ्यासोबत रात्री ८ नंतर पोस्टिंगच्या ठिकाणी जाऊन पाहावे. स्टेशनपासून चालत चाळीस मिनिटांपेक्षा जास्त दूर असलेली पोस्टिंग टाळावी.",
    "Placement assistance": "नोकरीचे सहाय्य",
    "Covers private hospitals, clinics and diagnostic laboratories. Very often the practice that trained a student for twenty months is the one that hires them.":
        "खाजगी हॉस्पिटल, क्लिनिक व डायग्नोस्टिक प्रयोगशाळांपुरते. ज्या ठिकाणी विद्यार्थ्याने वीस महिने प्रशिक्षण घेतले, तेच बहुतेक वेळा त्याला कामावर ठेवते.",
    "Scope of our placement assistance": "आमच्या नोकरी सहाय्याची व्याप्ती",
    "guarantee": "हमी देतो", "not": "नाही",
    "69 hospitals and 69 laboratories": "६९ हॉस्पिटल व ६९ प्रयोगशाळा",
    "The organisations that have taken our students on posting or employed them after qualifying. Named here so you can check them rather than take a placement figure on trust.":
        "ज्या संस्थांनी आमच्या विद्यार्थ्यांना पोस्टिंगवर घेतले किंवा कोर्सनंतर नोकरी दिली त्यांची नावे. केवळ आकडा सांगण्यापेक्षा तुम्हाला स्वतः तपासता यावे म्हणून नावे दिली आहेत.",
    "Listing reproduced from the institute's prospectus. Inclusion records that a student has been posted or placed there; it does not imply a standing vacancy, nor a commercial partnership.":
        "ही यादी संस्थेच्या प्रॉस्पेक्टसमधून घेतली आहे. नावाचा अर्थ तेथे विद्यार्थ्याची पोस्टिंग झाली किंवा नोकरी मिळाली एवढाच आहे; तेथे सध्या जागा रिक्त आहे किंवा व्यावसायिक भागीदारी आहे असा नाही.",
    "Students on public health campaigns": "सार्वजनिक आरोग्य मोहिमांमध्ये विद्यार्थी",
    "Our students work the BMC Pulse Polio vaccination campaign and Covid-19 vaccination drives — supervised public health experience that does not appear on any syllabus.":
        "आमचे विद्यार्थी बी.एम.सी. च्या पल्स पोलिओ लसीकरण मोहिमेत व कोविड-१९ लसीकरण मोहिमेत काम करतात — कोणत्याही अभ्यासक्रमात न बसणारा, देखरेखीखालील सार्वजनिक आरोग्याचा अनुभव.",
    "Letters from graduates, and what they earn": "विद्यार्थ्यांची पत्रे, आणि त्यांचा पगार",
    "Reproduced from the institute's prospectus with the writers' letters as submitted. Salaries are those reported by each graduate at the time of writing and are not a guarantee of earnings — what you are offered depends on the employer, the role and your own performance.":
        "संस्थेच्या प्रॉस्पेक्टसमधून, विद्यार्थ्यांनी लिहिलेली पत्रे जशीच्या तशी. पगाराचे आकडे लिहिण्याच्या वेळी त्या-त्या विद्यार्थ्याने सांगितलेले आहेत आणि ती कमाईची हमी नाही — तुम्हाला काय मिळेल हे नियोक्ता, पद आणि तुमच्या कामावर अवलंबून असते.",
    "Ask us about placement before you enrol.": "प्रवेशापूर्वी नोकरीविषयी आम्हाला विचारा.",
    "Ask which practices our students are currently posted to, and what our recent graduates are doing now. We would rather answer that at counselling than have you take it on trust.":
        "सध्या आमच्या विद्यार्थ्यांची पोस्टिंग कुठे आहे आणि अलीकडचे विद्यार्थी आता काय करत आहेत हे विचारा. हे केवळ विश्वासावर सोडण्यापेक्षा समुपदेशनात उत्तर देणे आम्हाला योग्य वाटते.",
})

# ---------------------------------------------------------------- contact / founder / misc
MR.update({
    "Come and see us in Dadar.": "दादर येथे आम्हाला भेटा.",
    "Telephone first to confirm counselling hours, then visit with a parent or guardian. We are a short walk from Dadar station, opposite Plaza.":
        "आधी फोन करून समुपदेशनाची वेळ निश्चित करा, नंतर पालकांसह भेटा. आम्ही दादर स्टेशनपासून थोड्याच अंतरावर, प्लाझा समोर आहोत.",
    "Send us your details": "तुमची माहिती पाठवा",
    "Tell us your last examination result and the course you are considering. A counsellor will reply the same working day and confirm whether you are eligible.":
        "शेवटच्या परीक्षेचा निकाल आणि कोणता कोर्स करायचा आहे ते कळवा. समुपदेशक त्याच कामकाजाच्या दिवशी उत्तर देऊन तुमची पात्रता निश्चित करतील.",
    "Dadar (West)": "दादर (प)",
    "Opposite Plaza, a short walk from Dadar station": "प्लाझा समोर, दादर स्टेशनपासून थोड्याच अंतरावर",
    "203 Akanksha, Opposite Plaza, Dadar (West), Mumbai 400 028 · nearest station Dadar.":
        "२०३ आकांक्षा, प्लाझा समोर, दादर (प), मुंबई ४०० ०२८ · जवळचे स्टेशन दादर.",
    "Diploma in Patient Care (DPC / DPCA)": "डिप्लोमा इन पेशंट केअर (DPC / DPCA)",
    "Diploma in Operation Theatre Technician (DOTT)": "डिप्लोमा इन ऑपरेशन थिएटर टेक्निशियन (DOTT)",
    "Diploma in Optometry (DOPTO)": "डिप्लोमा इन ऑप्टोमेट्री (DOPTO)",
    "Diploma in Medical Lab Technology (DMLT)": "डिप्लोमा इन मेडिकल लॅब टेक्नॉलॉजी (DMLT)",
    "The institute carries his name because he built it, teaches in it, and wrote most of the books our students learn from.":
        "संस्थेला त्यांचे नाव आहे कारण त्यांनी ती उभी केली, ते तिथे शिकवतात, आणि आमचे विद्यार्थी वापरतात ती बहुतेक पुस्तके त्यांनीच लिहिली आहेत.",
    "Need to discuss this?": "याविषयी बोलायचे आहे?",
    "Speak to us first": "आधी आमच्याशी बोला",
    "If circumstances have changed and you are thinking of withdrawing, contact the institute before the deadline passes rather than after. The slabs above are date-based and cannot be applied retrospectively.":
        "परिस्थिती बदलली असेल आणि प्रवेश रद्द करण्याचा विचार असेल तर अंतिम तारीख उलटून गेल्यावर नव्हे तर आधीच संस्थेशी संपर्क साधा. वरील टप्पे तारखेवर आधारित आहेत आणि पूर्वलक्षी प्रभावाने लागू होत नाहीत.",
    "Change of course before the course begins: ₹500. After it begins: ₹1,000 per month.":
        "कोर्स सुरू होण्यापूर्वी कोर्स बदलल्यास: ₹500. सुरू झाल्यानंतर: प्रति महिना ₹1,000.",
    "Failure to appear for the yearly final examination: 40% extra fee to re-register and re-examine.":
        "वार्षिक अंतिम परीक्षेला गैरहजर राहिल्यास: पुन्हा नोंदणी व परीक्षेसाठी 40% जास्त फी.",
    "Late instalment: 10% penalty per month; 12% interest applies on late fees.":
        "हप्ता उशिरा भरल्यास: दरमहा 10% दंड; उशिरा फीवर 12% व्याज लागते.",
    "Cheque returned unpaid by the bank: ₹500.": "बँकेने चेक न वटता परत केल्यास: ₹500.",
    "No refund is given once one month has passed from the commencement of the course":
        "कोर्स सुरू होऊन एक महिना उलटल्यानंतर कोणताही परतावा दिला जात नाही",
    "no refund is given at all where admission is taken after 25 September.":
        "२५ सप्टेंबरनंतर प्रवेश घेतल्यास कोणताही परतावा मिळत नाही.",
    "12th Science pass students": "१२ वी विज्ञान उत्तीर्ण विद्यार्थी",
    "B.Voc and Advanced Diploma": "B.Voc व अ‍ॅडव्हान्स्ड डिप्लोमा",
    "B.Voc — regular, 3 years": "B.Voc — नियमित, ३ वर्षे",
    "B.Voc — lateral entry, 2 years": "B.Voc — लॅटरल एंट्री, २ वर्षे",
    "3 yrs": "३ वर्षे", "2 yrs": "२ वर्षे", "1 yr": "१ वर्ष",
    "25 September 2026": "२५ सप्टेंबर 2026", "1 March 2027": "१ मार्च 2027",
    "25 September 2027": "२५ सप्टेंबर 2027", "1 April 2028": "१ एप्रिल 2028",
    "Specimen shown for illustration. The holder's name, register number, photograph and QR code have been redacted from this scan. Certificates are collected within one month of convocation.":
        "नमुना केवळ माहितीसाठी. या प्रतीतून धारकाचे नाव, नोंदणी क्रमांक, फोटो व QR कोड काढून टाकले आहेत. प्रमाणपत्र पदवीदान समारंभानंतर एका महिन्याच्या आत घ्यावे.",
    "The fee is one number; this is the other. Letters from our own graduates stating where they work and what they are paid — the figures are theirs, not ours. Reported salaries across all 14 letters run from ₹10,000 for a recent starter to ₹50,000 for a graduate of 2005.":
        "फी हा एक आकडा; हा दुसरा. आमच्याच विद्यार्थ्यांची पत्रे — ते कुठे काम करतात आणि किती पगार मिळतो हे त्यांनीच लिहिले आहे. सर्व 14 पत्रांतील पगार नुकत्याच सुरुवात केलेल्यासाठी ₹10,000 पासून 2005 सालच्या विद्यार्थिनीसाठी ₹50,000 पर्यंत आहेत.",
})

# certificate course names
for _en, _mr in [
    ("Blood Banking", "ब्लड बँकिंग"), ("Medical Lab Technician", "मेडिकल लॅब टेक्निशियन"),
    ("Nutrition", "न्यूट्रिशन"), ("Operation Theatre Technician", "ऑपरेशन थिएटर टेक्निशियन"),
    ("Dietician", "डायटीशियन"), ("X-Ray Technician", "एक्स-रे टेक्निशियन"),
    ("Optometry", "ऑप्टोमेट्री"), ("ECG Technician", "ई.सी.जी. टेक्निशियन"),
    ("Medical Records", "मेडिकल रेकॉर्ड्स"), ("Hospital Management", "हॉस्पिटल मॅनेजमेंट"),
    ("Ayurvedic Massage", "आयुर्वेदिक मसाज"), ("Ayurvedic Panchakarma", "आयुर्वेदिक पंचकर्म"),
]:
    MR["Certificate / Diploma in " + _en] = "सर्टिफिकेट / डिप्लोमा इन " + _mr

# per-course fee paragraphs
for _fee, _adm, _place in [("60,000", "12,000", "nursing home or hospital"),
                           ("68,000", "14,000", "laboratory"),
                           ("37,500", "15,000", "optician's practice or eye clinic")]:
    MR[f"The course fee is ₹{_fee}, inclusive of textbooks, workbooks, notes, equipment, examination fee, "
       f"registration and identity card. ₹{_adm} is payable at admission; the balance is staged in "
       f"instalments, and once your posting begins the monthly instalment is deducted from your stipend and "
       f"remitted to the institute directly by the doctor."] = (
        f"कोर्स फी ₹{_fee} आहे, ज्यात पाठ्यपुस्तके, कार्यपुस्तिका, नोट्स, साहित्य, परीक्षा फी, नोंदणी व "
        f"ओळखपत्र यांचा समावेश आहे. प्रवेशाच्या वेळी ₹{_adm} भरावे लागतात; उर्वरित रक्कम हप्त्यांमध्ये "
        f"भरायची असते, आणि पोस्टिंग सुरू झाल्यावर मासिक हप्ता स्टायपेंडमधून वजा करून डॉक्टर थेट संस्थेला पाठवतात.")

for _loc, _mr_loc in [("nursing home or hospital", "नर्सिंग होम किंवा हॉस्पिटल"),
                      ("laboratory", "प्रयोगशाळा"),
                      ("hospital operation theatre", "हॉस्पिटलच्या ऑपरेशन थिएटर"),
                      ("optician's practice or eye clinic", "ऑप्टिशियन किंवा नेत्र क्लिनिक")]:
    MR[f"The first four months are classroom training at our Dadar premises, with a compulsory test after "
       f"every chapter that counts towards your internal assessment. From the fifth month you move to a "
       f"full-time posting in a working {_loc}, where you work under a practising doctor and draw a monthly "
       f"stipend."] = (
        f"पहिले चार महिने आमच्या दादर येथील वास्तूत वर्गातील प्रशिक्षण असते, प्रत्येक प्रकरणानंतर अनिवार्य "
        f"चाचणी असते आणि तिचे गुण अंतर्गत मूल्यमापनात धरले जातात. पाचव्या महिन्यापासून प्रत्यक्ष चालू असलेल्या "
        f"{_mr_loc} मध्ये पूर्णवेळ पोस्टिंग सुरू होते, जिथे तुम्ही प्रॅक्टिस करणाऱ्या डॉक्टरांच्या "
        f"देखरेखीखाली काम करता आणि मासिक स्टायपेंड मिळवता.")

MR.update({
    "Stipend is paid by the host laboratory and may vary above or below these figures according to your work. Uniform and apron are purchased by the student, and entry to duty is refused without them.":
        "स्टायपेंड संबंधित प्रयोगशाळेकडून दिला जातो आणि कामाप्रमाणे तो या आकड्यांपेक्षा कमी-जास्त होऊ शकतो. गणवेश व एप्रन विद्यार्थ्याने स्वखर्चाने घ्यावा; त्याशिवाय ड्युटीवर प्रवेश दिला जात नाही.",
    "This is our lowest-fee diploma at ₹37,500. Postings are with opticians and eye clinics rather than general hospitals.":
        "₹37,500 फी असलेला हा आमचा सर्वात कमी फीचा डिप्लोमा आहे. पोस्टिंग सर्वसाधारण हॉस्पिटलऐवजी ऑप्टिशियन व नेत्र क्लिनिकमध्ये असते.",
    "This is our most subscribed course, and requires 12th pass or fail. Students are expected to work in two shifts or on break duty during the posting.":
        "हा आमचा सर्वाधिक मागणी असलेला कोर्स असून त्यासाठी १२ वी पास किंवा नापास आवश्यक आहे. पोस्टिंगदरम्यान विद्यार्थ्यांनी दोन शिफ्टमध्ये किंवा ब्रेक ड्युटीवर काम करणे अपेक्षित आहे.",
    "DPC / DPCA / DOTT / DOPTO": "DPC / DPCA / DOTT / DOPTO",
    "TOTAL FEE ₹60,000": "एकूण फी ₹60,000", "TOTAL FEE ₹68,000": "एकूण फी ₹68,000",
    "TOTAL FEE ₹20,000": "एकूण फी ₹20,000",
})

# ---------------------------------------------------------------- founder page
MR.update({
    "A practising doctor, not an administrator": "प्रशासक नव्हे, प्रत्यक्ष प्रॅक्टिस करणारे डॉक्टर",
    "Dr. Hemant Raje Gaikwad qualified MBBS, took his DOMS in ophthalmology and went on to a PhD. He founded this institute in 1996 on a straightforward premise: Mumbai's nursing homes, laboratories and clinics needed trained technicians far more than they needed more theory graduates, and the fastest honest route into that work was to put students on a real hospital floor and pay them while they learned.":
        "डॉ. हेमंत राजे गायकवाड यांनी MBBS केले, नेत्रविज्ञानात DOMS घेतले आणि पुढे PhD मिळवली. १९९६ साली त्यांनी एका साध्या विचारातून ही संस्था सुरू केली: मुंबईतील नर्सिंग होम, प्रयोगशाळा व क्लिनिकना केवळ सिद्धांत शिकलेल्या पदवीधरांपेक्षा प्रशिक्षित टेक्निशियनची कितीतरी जास्त गरज होती, आणि त्या कामापर्यंत पोहोचण्याचा प्रामाणिक व जलद मार्ग म्हणजे विद्यार्थ्यांना प्रत्यक्ष हॉस्पिटलमध्ये उभे करणे आणि शिकताना त्यांना पगार देणे.",
    "Three decades later that is still how the courses run — four months in the classroom, twenty months on posting, under a practising doctor.":
        "तीन दशकांनंतरही कोर्सेस त्याच पद्धतीने चालतात — चार महिने वर्गात, वीस महिने पोस्टिंगवर, प्रॅक्टिस करणाऱ्या डॉक्टरांच्या देखरेखीखाली.",
    "He wrote the textbooks": "त्यांनी स्वतः पाठ्यपुस्तके लिहिली",
    "Rather than set students texts written for medical undergraduates, he wrote his own — more than a dozen manuals covering anatomy, surgery, pharmacology, obstetrics, paediatrics, laboratory practice, blood banking, nutrition and instruments, including a textbook of optometry in Marathi. They are the books used on our courses.":
        "वैद्यकीय पदवीच्या विद्यार्थ्यांसाठी लिहिलेली पुस्तके लावण्याऐवजी त्यांनी स्वतःची पुस्तके लिहिली — शरीररचना, शस्त्रक्रिया, औषधशास्त्र, प्रसूतिशास्त्र, बालरोग, प्रयोगशाळा कार्य, रक्तपेढी, पोषण व उपकरणे यांवरील डझनभराहून अधिक पुस्तके, त्यात मराठीतील ऑप्टोमेट्रीच्या पाठ्यपुस्तकाचाही समावेश आहे. आमच्या कोर्सेसमध्ये हीच पुस्तके वापरली जातात.",
    "Beyond the institute": "संस्थेपलीकडे",
    "Bharat Karmasri Award": "भारत कर्मश्री पुरस्कार",
    "Author of": "लेखक —",
    "Public health service": "सार्वजनिक आरोग्य सेवा",
    "The manuals our students learn from": "आमचे विद्यार्थी शिकतात ती पुस्तके",
    "Written specifically for paramedical students working in nursing homes and laboratories, rather than adapted from medical-undergraduate texts. Included in your course fee.":
        "वैद्यकीय पदवीच्या पुस्तकांतून घेतलेली नव्हे, तर नर्सिंग होम व प्रयोगशाळांमध्ये काम करणाऱ्या पॅरामेडिकल विद्यार्थ्यांसाठी खास लिहिलेली पुस्तके. तुमच्या कोर्स फीमध्ये समाविष्ट.",
    "Awards and public service": "पुरस्कार व सामाजिक कार्य",
    "Meet him at the institute.": "संस्थेत त्यांना भेटा.",
    "The director takes counselling visits himself where he can. Telephone first to confirm when he is available, and bring a parent or guardian.":
        "शक्य असेल तेव्हा संचालक स्वतः समुपदेशन भेटी घेतात. ते कधी उपलब्ध आहेत हे आधी फोनवरून विचारा, आणि पालकांना सोबत आणा.",
    "Dr. Hemant Raje Gaikwad in his capacity as Commandant, Home Guards.":
        "डॉ. हेमंत राजे गायकवाड, होमगार्डचे कमांडंट म्हणून.",
    "Also written by Dr. Hemant Raje Gaikwad: Manual of Paediatrics, Manual of General Instruments, Manual of Nutrition, Manual of Blood Banking, Manual of Medicine for Nursing Homes, Manual of English Speaking.":
        "डॉ. हेमंत राजे गायकवाड यांनी लिहिलेली इतर पुस्तके: Manual of Paediatrics, Manual of General Instruments, Manual of Nutrition, Manual of Blood Banking, Manual of Medicine for Nursing Homes, Manual of English Speaking.",
})

# ---------------------------------------------------------------- accreditation page
MR.update({
    "Who certifies what we teach.": "आम्ही जे शिकवतो त्याला मान्यता कोणाची.",
    "Four independent certifications sit behind the diplomas awarded here. The certificates themselves are reproduced on this page — ask to see the originals at your counselling visit.":
        "येथे दिल्या जाणाऱ्या डिप्लोमांमागे चार स्वतंत्र मान्यता आहेत. प्रमाणपत्रे स्वतः या पानावर दिली आहेत — समुपदेशन भेटीच्या वेळी मूळ प्रती पाहण्यास मागा.",
    "National development agency promoted by the Government of India in 1952, its constitution approved unanimously by the Indian Parliament. Every diploma is awarded under this certification.":
        "भारत सरकारने १९५२ साली पुरस्कृत केलेली राष्ट्रीय विकास संस्था, जिची घटना भारतीय संसदेने एकमताने मंजूर केली. प्रत्येक डिप्लोमा याच मान्यतेखाली दिला जातो.",
    "Certificate of Registration for the institute's Quality Management System.":
        "संस्थेच्या गुणवत्ता व्यवस्थापन प्रणालीचे नोंदणी प्रमाणपत्र.",
    "Accredited institute of HLACT International for the period January 2017 to December 2027, against international education standards.":
        "जानेवारी २०१७ ते डिसेंबर २०२७ या कालावधीसाठी, आंतरराष्ट्रीय शैक्षणिक मानकांनुसार HLACT International ची मान्यताप्राप्त संस्था.",
    "Authorised Skill Institute of the World Skill Council.": "World Skill Council ची अधिकृत कौशल्य संस्था.",
    "The documents themselves": "प्रमाणपत्रे स्वतः",
    "Reproduced from the institute's prospectus. Originals are available for inspection at the Dadar premises.":
        "संस्थेच्या प्रॉस्पेक्टसमधून घेतलेली. मूळ प्रती दादर येथील कार्यालयात पाहण्यासाठी उपलब्ध आहेत.",
    "What these do and do not cover": "यांची व्याप्ती काय आहे आणि काय नाही",
    "These certifications cover the institute and the diplomas it awards. They are not a substitute for statutory professional registration. In particular, the Diploma in Patient Care and Diploma in Patient Care Assistant have":
        "या मान्यता संस्थेला व ती देत असलेल्या डिप्लोमांना लागू आहेत. त्या वैधानिक व्यावसायिक नोंदणीला पर्याय नाहीत. विशेषतः, डिप्लोमा इन पेशंट केअर व डिप्लोमा इन पेशंट केअर असिस्टंट यांचा",
    "no affiliation with the Indian Nursing Council": "इंडियन नर्सिंग कौन्सिलशी संबंध नाही",
    "Ask to see the originals.": "मूळ प्रती पाहण्यास मागा.",
    "Every certificate reproduced here is held at the institute. Bring a parent or guardian to a counselling visit and ask to see them.":
        "येथे दिलेले प्रत्येक प्रमाणपत्र संस्थेकडे आहे. समुपदेशन भेटीला पालकांना सोबत आणा आणि ती पाहण्यास मागा.",
    "ISO 9001": "ISO 9001",
})

# ---------------------------------------------------------------- gallery page
MR.update({
    "There is a life here beyond the attendance register.": "हजेरीपटाच्या पलीकडेही येथे एक जीवन आहे.",
    "We ask a great deal of our students — ninety per cent attendance, uniform on duty, night shifts. We also make room for Ganeshotsav, sports day, cooking competitions and a proper convocation. Both are true, and both belong on this page.":
        "आम्ही विद्यार्थ्यांकडून बरेच काही मागतो — नव्वद टक्के हजेरी, ड्युटीवर गणवेश, नाईट शिफ्ट. त्याचबरोबर गणेशोत्सव, क्रीडा दिन, पाककला स्पर्धा आणि रीतसर पदवीदान समारंभ यांनाही जागा देतो. दोन्ही गोष्टी खऱ्या आहेत, आणि दोन्हींना या पानावर स्थान आहे.",
    "Classroom and practical work": "वर्ग व प्रात्यक्षिक कार्य",
    "The first four months at the Dadar premises: lectures, practical laboratory sessions and the chapter-end tests that count towards internal assessment.":
        "दादर येथील वास्तूत पहिले चार महिने: व्याख्याने, प्रयोगशाळेतील प्रात्यक्षिके आणि अंतर्गत मूल्यमापनात धरल्या जाणाऱ्या प्रकरणानंतरच्या चाचण्या.",
    "Hospital postings": "हॉस्पिटल पोस्टिंग",
    "On duty across Mumbai": "मुंबईभर ड्युटीवर",
    "From the fifth month, students work full shifts in nursing homes, diagnostic laboratories, operation theatres and opticians' practices under a practising doctor.":
        "पाचव्या महिन्यापासून विद्यार्थी नर्सिंग होम, डायग्नोस्टिक प्रयोगशाळा, ऑपरेशन थिएटर व ऑप्टिशियनकडे प्रॅक्टिस करणाऱ्या डॉक्टरांच्या देखरेखीखाली पूर्ण शिफ्ट काम करतात.",
    "Festivals, competitions and celebration": "सण, स्पर्धा व उत्सव",
    "Funded entirely from fine collections — not one rupee of it is used by the institute for itself. Ganeshotsav, Dassehra, Diwali, Eid, Christmas, New Year, Republic Day and Gurupurnima are all marked here.":
        "संपूर्णपणे दंडाच्या रकमेतून — त्यातील एक रुपयाही संस्था स्वतःसाठी वापरत नाही. गणेशोत्सव, दसरा, दिवाळी, ईद, ख्रिसमस, नवीन वर्ष, प्रजासत्ताक दिन व गुरुपौर्णिमा हे सर्व येथे साजरे होतात.",
    "Beyond the syllabus": "अभ्यासक्रमापलीकडे",
    "Activities run alongside the course and included in the fee — no separate charge.":
        "कोर्ससोबत चालणारे उपक्रम, फीमध्ये समाविष्ट — वेगळे शुल्क नाही.",
    "The day the diploma is awarded": "डिप्लोमा मिळण्याचा दिवस",
    "Held in August or September each year, subject to results and hall availability. Certificates are awarded under Bharat Sevak Samaj certification, and families are welcome.":
        "दरवर्षी ऑगस्ट किंवा सप्टेंबरमध्ये, निकाल व सभागृहाच्या उपलब्धतेनुसार. प्रमाणपत्रे भारत सेवक समाजाच्या मान्यतेखाली दिली जातात, आणि कुटुंबीयांचे स्वागत आहे.",
    "A note on these photographs": "या छायाचित्रांविषयी एक सूचना",
    "Come and see it for yourself.": "स्वतः येऊन पहा.",
    "Photographs only go so far. Telephone to arrange a counselling visit and see the premises, meet the staff and ask whatever you like.":
        "छायाचित्रे एका मर्यादेपर्यंतच सांगू शकतात. फोन करून समुपदेशन भेटीची वेळ ठरवा, वास्तू पहा, कर्मचाऱ्यांना भेटा आणि हवे ते विचारा.",
})

# ---------------------------------------------------------------- 404 + misc
MR.update({
    "Error 404": "एरर ४०४",
    "This page has moved, or never existed.": "हे पान हलवले आहे, किंवा ते कधीच नव्हते.",
    "That happens when a link is out of date or an address is mistyped. Everything on the site is reachable from the links below — or telephone the institute and we will point you to it.":
        "लिंक जुनी असल्यास किंवा पत्ता चुकीचा टाइप झाल्यास असे होते. साइटवरील सर्व काही खालील दुव्यांवरून मिळेल — किंवा संस्थेला फोन करा, आम्ही मार्ग दाखवू.",
    "Back to the home page": "मुख्यपृष्ठावर परत",
    "Where you may have been going": "तुम्ही कदाचित येथे जात असाल",
    "The pages people look for most": "सर्वाधिक शोधली जाणारी पाने",
    "What we teach": "आम्ही काय शिकवतो",
    "Four two-year stipendiary diplomas, twelve one-year certificates for working technicians, and a B.Voc degree pathway.":
        "स्टायपेंडसह दोन वर्षांचे चार डिप्लोमा, कार्यरत टेक्निशियनसाठी एक वर्षाची बारा सर्टिफिकेट, आणि B.Voc पदवी मार्ग.",
    "Browse all courses →": "सर्व कोर्सेस पहा →",
    "What it costs": "किती खर्च येतो",
    "The full fee schedule for every course, the stipend ladder against it, instalment dates and the refund policy.":
        "प्रत्येक कोर्सचे संपूर्ण फी वेळापत्रक, त्यासमोरील स्टायपेंड, हप्त्यांच्या तारखा व परतावा नियम.",
    "See the fee schedule →": "फी वेळापत्रक पहा →",
    "The four-step admission process, the document checklist and the institute rules you agree to on admission.":
        "चार टप्प्यांची प्रवेश प्रक्रिया, कागदपत्रांची यादी आणि प्रवेशाच्या वेळी मान्य कराव्या लागणाऱ्या संस्थेच्या अटी.",
    "Read the process →": "प्रक्रिया वाचा →",
    "Diploma pages": "डिप्लोमा पाने", "Other courses": "इतर कोर्सेस",
    "Speak to us": "आमच्याशी बोला",
    "Counselling is free and carries no obligation.": "समुपदेशन मोफत आहे व त्याचे कोणतेही बंधन नाही.",
    "Contact page": "संपर्क पान",
    "Across Mumbai": "मुंबईभर",
    "Hospitals & nursing homes": "हॉस्पिटल व नर्सिंग होम",
    "Laboratories & diagnostic centres": "प्रयोगशाळा व डायग्नोस्टिक सेंटर",
    "Textbooks & workbooks": "पाठ्यपुस्तके व कार्यपुस्तिका",
    "Medical Laboratory Technology": "मेडिकल लॅबोरेटरी टेक्नॉलॉजी",
    "Placement assistance applies to the four two-year diploma courses only, and what we":
        "नोकरीचे सहाय्य फक्त दोन वर्षांच्या चार डिप्लोमा कोर्सेसना लागू आहे, आणि आम्ही ज्याची",
    "Written by our own students after they were placed, and reproduced here exactly as they wrote them. The English beside each letter is a translation of the Marathi; the salary is the figure the writer states.":
        "नोकरी मिळाल्यानंतर आमच्याच विद्यार्थ्यांनी लिहिलेली पत्रे, जशीच्या तशी येथे दिली आहेत. पगाराचा आकडा त्या-त्या विद्यार्थ्याने लिहिलेला आहे.",
})

MR["The practical and posting photographs on this page are from the institute's own archive, taken at the practices where our students train. Panels still marked with an icon are awaiting a photograph — they are drawn that way on purpose, so nothing here is mistaken for a picture of an event we have not photographed. If you appear in any image on this page and would like it removed, write to"] = "या पानावरील प्रात्यक्षिक व पोस्टिंगची छायाचित्रे संस्थेच्या स्वतःच्या संग्रहातील असून, आमचे विद्यार्थी जेथे प्रशिक्षण घेतात तेथे काढलेली आहेत. ज्या चौकटींवर अजून चिन्ह आहे तेथे छायाचित्र यायचे आहे — ते मुद्दाम तसे ठेवले आहे, जेणेकरून न काढलेल्या कार्यक्रमाचे छायाचित्र आहे असा गैरसमज होऊ नये. या पानावरील कोणत्याही छायाचित्रात तुम्ही असाल आणि ते काढून टाकायचे असेल, तर येथे लिहा"
