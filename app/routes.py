from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

PROGRAMME_HIGHLIGHTS = [
    {
        "title": "Interdisciplinary Focus",
        "body": "Blend media theory, communication strategy, and interactive design with practical production skills.",
    },
    {
        "title": "Hands-on Studio Learning",
        "body": "Build digital storytelling, UX, and multimedia prototyping skills through project-based coursework.",
    },
    {
        "title": "Industry Relevance",
        "body": "Apply creative media solutions to business communication, training, and audience engagement.",
    },
]

CURRICULUM_BLOCKS = [
    {
        "name": "Foundation",
        "items": [
            "Communication and media theory",
            "Digital media ecosystems",
            "Audience and platform analytics",
        ],
    },
    {
        "name": "Design and Production",
        "items": [
            "Interactive multimedia design",
            "User interface and experience principles",
            "Visual storytelling and prototyping",
        ],
    },
    {
        "name": "Application",
        "items": [
            "Media innovation project",
            "Campaign and content strategy",
            "Capstone-ready portfolio development",
        ],
    },
]

FAQ_ITEMS = [
    {
        "question": "Who should apply to the programme?",
        "answer": "Applicants with interests in communication, digital products, media innovation, and storytelling are welcome.",
    },
    {
        "question": "Is prior coding experience required?",
        "answer": "No. The curriculum supports learners from mixed backgrounds and builds technical fluency progressively.",
    },
    {
        "question": "What are graduates prepared for?",
        "answer": "Roles in digital communication, creative technology, media strategy, UX content, and multimedia production.",
    },
]

FACULTY_EXAMPLES = [
    "Communication and media studies scholars",
    "Digital journalism and storytelling practitioners",
    "Design and interaction specialists",
    "Industry-connected instructors and mentors",
]

STUDENT_ALUMNI_SECTIONS = [
    "Student awards and showcases",
    "Graduation projects",
    "Alumni voices and career pathways",
    "Community and alumni committee activities",
]


@main_bp.route("/")
def home():
    return render_template(
        "home.html",
        page_title="MSc in New Media | CUHK",
        highlights=PROGRAMME_HIGHLIGHTS,
        curriculum=CURRICULUM_BLOCKS,
        faqs=FAQ_ITEMS,
        faculty=FACULTY_EXAMPLES,
        student_alumni=STUDENT_ALUMNI_SECTIONS,
    )


@main_bp.route("/programme")
def programme():
    return render_template(
        "programme.html",
        page_title="Programme Overview | MSc in New Media",
        highlights=PROGRAMME_HIGHLIGHTS,
    )


@main_bp.route("/curriculum")
def curriculum():
    return render_template(
        "curriculum.html",
        page_title="Curriculum | MSc in New Media",
        curriculum=CURRICULUM_BLOCKS,
    )


@main_bp.route("/admissions")
def admissions():
    return render_template(
        "admissions.html",
        page_title="Admissions and FAQ | MSc in New Media",
        faqs=FAQ_ITEMS,
    )


@main_bp.route("/faculty")
def faculty():
    return render_template(
        "faculty.html",
        page_title="Faculty | MSc in New Media",
        faculty=FACULTY_EXAMPLES,
    )


@main_bp.route("/research")
def research():
    return render_template(
        "research.html",
        page_title="Research | MSc in New Media",
    )


@main_bp.route("/students-alumni")
def students_alumni():
    return render_template(
        "students_alumni.html",
        page_title="Students and Alumni | MSc in New Media",
        student_alumni=STUDENT_ALUMNI_SECTIONS,
    )


@main_bp.route("/contact")
def contact():
    return render_template(
        "contact.html",
        page_title="Contact | MSc in New Media",
    )

