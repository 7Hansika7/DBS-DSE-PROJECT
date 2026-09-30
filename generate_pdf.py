#!/usr/bin/env python3
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#0284c7"))

        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "EYE OF ODIN")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawString(120, 11 * inch - 36, "— Project Description & Output Documentation")
            self.drawRightString(8.5 * inch - 54, 11 * inch - 36, "DBS-DSE-PROJECT")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.75)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)

        # Running Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.75)
        self.line(54, 46, 8.5 * inch - 54, 46)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(54, 32, "Confidential Academic Reference  •  7Hansika7 / DBS-DSE-PROJECT")
        self.drawRightString(8.5 * inch - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0284c7"),
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1e40af"),
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceAfter=5
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#1e293b")
    )

    table_header_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TB',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1e293b")
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0f172a")
    )

    story = []

    # Title & Subtitle Banner
    story.append(Paragraph("EYE OF ODIN: 3D Campus Lost & Found Tracker", title_style))
    story.append(Paragraph("System Architecture, Multi-Modal AI Engine & Comprehensive Output Documentation", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#0284c7"), spaceBefore=0, spaceAfter=8))

    # Metadata Table
    meta_data = [
        [Paragraph("<b>Project Title:</b>", table_body_style), Paragraph("Eye of Odin: Lost & Found 3D Tracker", table_body_style),
         Paragraph("<b>Repository:</b>", table_body_style), Paragraph("7Hansika7 / DBS-DSE-PROJECT", table_body_style)],
        [Paragraph("<b>Tech Stack:</b>", table_body_style), Paragraph("Node.js (Native REST) + Three.js WebGL", table_body_style),
         Paragraph("<b>Target Domain:</b>", table_body_style), Paragraph("University Campus Safety & Recovery", table_body_style)],
        [Paragraph("<b>Dependencies:</b>", table_body_style), Paragraph("Zero external npm packages (Pure JS)", table_body_style),
         Paragraph("<b>Documentation:</b>", table_body_style), Paragraph("Release v1.0 (Academic Report)", table_body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[1.1*inch, 2.45*inch, 1.1*inch, 2.45*inch])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    # SECTION 1: EXECUTIVE SUMMARY
    story.append(Paragraph("1. Executive Summary & Problem Formulation", h1_style))
    story.append(Paragraph(
        "University campuses are dense, high-traffic ecosystems where thousands of students, faculty, and visitors lose essential personal items daily—ranging from standard articles (water bottles, umbrellas) to high-consequence belongings (academic thesis laptops, research data drives, passports, prescription glasses, and vehicle keys).",
        body_style
    ))
    story.append(Paragraph(
        "Traditional campus lost-and-found desks face major operational bottlenecks: disjointed bulletin boards, poor communication between disparate campus departments, lack of urgency triage, and high vulnerability to fraudulent ownership claims. <b>Eye of Odin</b> solves these challenges by combining an interactive <b>Three.js 3D WebGL aperture interface</b> with an intelligent <b>5-Vector Multi-Modal AI Matching Engine</b>, an <b>Anti-Scam Claim Verification Protocol</b>, and an integrated <b>Campus Security Custody Locker Management System</b>.",
        body_style
    ))

    # Callout Box
    callout_content = [[Paragraph(
        "<b>Core Architecture Advantage:</b> Eye of Odin operates with <b>zero external npm dependencies</b> on the backend, ensuring instant portable deployment, zero-latency startup on Node.js, and an ultra-lightweight client-side 3D rendering pipeline capable of running smoothly on all standard university lab computers and mobile browsers.",
        callout_style
    )]]
    t_callout = Table(callout_content, colWidths=[7.1*inch])
    t_callout.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_callout)
    story.append(Spacer(1, 8))

    # SECTION 2: SYSTEM ARCHITECTURE
    story.append(Paragraph("2. System Architecture & Component Design", h1_style))
    story.append(Paragraph(
        "The project is partitioned into distinct modular layers ensuring clean separation of concerns, persistent state tracking, and fast query execution:",
        body_style
    ))

    arch_data = [
        [Paragraph("Tier / Module", table_header_style), Paragraph("Technologies", table_header_style), Paragraph("Functional Responsibilities", table_header_style)],
        [
            Paragraph("<b>Frontend 3D HUD Dock</b>", table_body_style),
            Paragraph("Three.js, WebGL, Vanilla ES6+, CSS Glassmorphism", table_body_style),
            Paragraph("Interactive 3D mechanical iris, orbital item meshes, live telemetry cards, scrollytelling dock, printable QR poster generator, Web Audio procedural SFX.", table_body_style)
        ],
        [
            Paragraph("<b>Backend REST Server</b>", table_body_style),
            Paragraph("Node.js Native HTTP, FileSystem, URL Modules", table_body_style),
            Paragraph("Zero-dependency microservice hosting static web assets, serving REST endpoints (/api/items, /api/stats, /api/claims), and handling CORS preflights.", table_body_style)
        ],
        [
            Paragraph("<b>Persistence Layer</b>", table_body_style),
            Paragraph("JSON Flat-File Database (items.json, claims.json)", table_body_style),
            Paragraph("ACID-like safe file write transactions, audit logging, item status lifecycle tracking (active, in_vault, reunited).", table_body_style)
        ],
        [
            Paragraph("<b>AI Matching Engine</b>", table_body_style),
            Paragraph("Vector Affinity Matrix & Jaccard Tokenizer", table_body_style),
            Paragraph("5-dimensional similarity computation matching newly reported items against existing database records with confidence percentages.", table_body_style)
        ]
    ]
    t_arch = Table(arch_data, colWidths=[1.7*inch, 1.9*inch, 3.5*inch])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_arch)
    story.append(PageBreak())

    # SECTION 3: 5-VECTOR AI MATCHING ENGINE
    story.append(Paragraph("3. Multi-Modal AI Similarity Matching Engine", h1_style))
    story.append(Paragraph(
        "To minimize search friction and automate pairing between lost reports and found items, the engine calculates a composite affinity score using five weighted dimensions:",
        body_style
    ))

    ai_weights = [
        [Paragraph("Vector Dimension", table_header_style), Paragraph("Weight", table_header_style), Paragraph("Algorithm & Computation Principle", table_header_style)],
        [
            Paragraph("<b>Category Match</b>", table_body_style),
            Paragraph("<b>30%</b>", table_body_style),
            Paragraph("Exact taxonomic equality + fallback to custom subcategories (Electronics, Books, ID Cards, Valuables).", table_body_style)
        ],
        [
            Paragraph("<b>Keywords & Semantics</b>", table_body_style),
            Paragraph("<b>25%</b>", table_body_style),
            Paragraph("Stop-word filtered tokenization with Jaccard coefficient overlap computed across title, description, and metadata tags.", table_body_style)
        ],
        [
            Paragraph("<b>Spatial Telemetry</b>", table_body_style),
            Paragraph("<b>20%</b>", table_body_style),
            Paragraph("Campus building coordinate proximity using Euclidean distance over 3D campus coordinates (sqrt(dx^2 + dz^2)).", table_body_style)
        ],
        [
            Paragraph("<b>Color Affinity</b>", table_body_style),
            Paragraph("<b>15%</b>", table_body_style),
            Paragraph("Hexadecimal RGB vector color delta distance combined with semantic color label matching.", table_body_style)
        ],
        [
            Paragraph("<b>Temporal Window</b>", table_body_style),
            Paragraph("<b>10%</b>", table_body_style),
            Paragraph("Exponential temporal decay scoring items reported within close proximity of the incident timestamp.", table_body_style)
        ]
    ]
    t_ai = Table(ai_weights, colWidths=[1.7*inch, 0.8*inch, 4.6*inch])
    t_ai.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e40af")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ai)
    story.append(Spacer(1, 10))

    # SECTION 4: DETAILED OUTPUT DESCRIPTION
    story.append(Paragraph("4. Detailed Output Description & Interface Walkthrough", h1_style))
    story.append(Paragraph(
        "This section documents the visual, interactive, and functional outputs produced by the system across each module and state of execution:",
        body_style
    ))

    outputs = [
        ("Output 1: 3D WebGL Holographic HUD & Odin Eye",
         "When launched, the browser renders an interactive 3D scene in the right viewport. A mechanical iris aperture pupil expands and contracts in response to mouse movement and scroll depth. Holographic concentric rings with runes rotate along the Z-axis, while five detailed 3D models (MacBook Pro, AirPods Pro, Brass Keyring, Student ID Badge, and Hydro Flask) orbit the central core. Hovering or clicking an item initiates orbital focus, displaying item telemetry."),

        ("Output 2: Priority-Coded Item Stream & Left HUD Dock",
         "The left side displays a glassmorphic dashboard with live item counts (Lost, Found, Reunited, Vault Custody) and recovery rate metrics (e.g., 91% Success Rate). Items are tagged with distinct priority badges:\n• CRITICAL (Red): Academic thesis laptops, passports, prescription glasses.\n• HIGH (Amber): Smartphones, keychains, transit passes.\n• STANDARD (Blue): Apparel, umbrellas, bottles, textbooks.\nFilters allow instant isolation by status, category, urgency, and keyword search."),

        ("Output 3: Cinema View Mode (Unobstructed Viewport)",
         "Clicking the '[Cinema View]' toggle smoothly collapses all HUD sidebars, overlays, and filter pills, providing an unobstructed 3D canvas for interactive exploration, presentation mode, or campus digital signage kiosk deployment."),

        ("Output 4: Multi-Step Lost & Found Reporting Wizard",
         "Users trigger a modal wizard to register an item. Outputs include:\n• Dynamic category selection with write-in custom tags.\n• Interactive campus map selector assigning building ID and specific room/spot coordinates.\n• Color swatch picker with automated semantic color labeling.\n• Secret Ownership Question prompt to establish anti-scam safeguards before publishing."),

        ("Output 5: Anti-Scam Claim Verification Protocol",
         "When a student clicks 'Claim Item', the system presents an ownership challenge (e.g., 'What sticker is on the laptop lid?' or 'Specify the last 4 digits of the serial ID'). The claimant's answer is recorded in claims.json, and contact info remains protected until the finder or security officer validates the response."),

        ("Output 6: Campus Security Custody Locker Manager",
         "For valuable or sensitive items handed into campus safety, the Admin Portal outputs a locker management matrix (e.g., Locker A-04, Locker B-12). Staff can check-in items, update custody status to 'in_vault', log student verification IDs, and mark items as 'reunited' upon verified pickup."),

        ("Output 7: Printable High-Resolution QR Poster Generator",
         "Clicking 'Generate Poster' dynamically formats a printable A4/Letter campus lost-and-found flyer. The output contains high-contrast typography, item specifications, location summary, and an auto-generated QR code linking directly to the digital claim modal.")
    ]

    for title, desc in outputs[:4]:
        story.append(Paragraph(title, h2_style))
        for line in desc.split("\n"):
            story.append(Paragraph(line, body_style))

    story.append(PageBreak())

    for title, desc in outputs[4:]:
        story.append(Paragraph(title, h2_style))
        for line in desc.split("\n"):
            story.append(Paragraph(line, body_style))

    story.append(Spacer(1, 10))

    # SECTION 5: REST API SPECIFICATION
    story.append(Paragraph("5. REST API Specification & Data Model", h1_style))
    story.append(Paragraph(
        "The backend implements zero-dependency endpoints communicating strictly in UTF-8 JSON with automated CORS support:",
        body_style
    ))

    api_endpoints = [
        [Paragraph("Endpoint", table_header_style), Paragraph("Method", table_header_style), Paragraph("Parameters / Body", table_header_style), Paragraph("Response Payload Description", table_header_style)],
        [
            Paragraph("<b>/api/health</b>", code_style), Paragraph("GET", table_body_style),
            Paragraph("None", table_body_style),
            Paragraph("Service status, uptime seconds, server timestamp.", table_body_style)
        ],
        [
            Paragraph("<b>/api/stats</b>", code_style), Paragraph("GET", table_body_style),
            Paragraph("None", table_body_style),
            Paragraph("Total counts (lost, found, reunited, in_vault) and recovery rate %.", table_body_style)
        ],
        [
            Paragraph("<b>/api/items</b>", code_style), Paragraph("GET", table_body_style),
            Paragraph("?type=&category=&priority=&q=", table_body_style),
            Paragraph("Array of filtered item objects matching query criteria.", table_body_style)
        ],
        [
            Paragraph("<b>/api/items</b>", code_style), Paragraph("POST", table_body_style),
            Paragraph("{ title, type, priority, category, ... }", table_body_style),
            Paragraph("Newly created item record with generated UUID timestamp.", table_body_style)
        ],
        [
            Paragraph("<b>/api/items/:id</b>", code_style), Paragraph("PATCH", table_body_style),
            Paragraph("{ status, custody, lockerId }", table_body_style),
            Paragraph("Updated item record reflecting modified state.", table_body_style)
        ],
        [
            Paragraph("<b>/api/claims</b>", code_style), Paragraph("POST", table_body_style),
            Paragraph("{ itemId, claimantName, answer }", table_body_style),
            Paragraph("Confirmation receipt and pending verification ID.", table_body_style)
        ],
        [
            Paragraph("<b>/api/items/match/:id</b>", code_style), Paragraph("GET", table_body_style),
            Paragraph("Item ID in URL path", table_body_style),
            Paragraph("Ranked matches sorted by 5-vector composite similarity score.", table_body_style)
        ]
    ]
    t_api = Table(api_endpoints, colWidths=[2.0*inch, 0.6*inch, 2.1*inch, 2.4*inch])
    t_api.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_api)
    story.append(Spacer(1, 10))

    # SECTION 6: EXECUTION & VERIFICATION
    story.append(Paragraph("6. Execution, Verification & Testing Instructions", h1_style))

    cmd_box = [
        [Paragraph(
            "<b>1. Launch Backend Server:</b><br/>"
            "<code>cd CODE/backend && node server.js</code><br/>"
            "<i>Server will listen on <b>http://localhost:5050</b> (or custom $PORT)</i><br/><br/>"
            "<b>2. Access Frontend Application:</b><br/>"
            "Open your browser and navigate to <b>http://localhost:5050</b>.<br/>"
            "The 3D WebGL viewport will initialize automatically alongside the live HUD dock.<br/><br/>"
            "<b>3. Test API Health & Stats:</b><br/>"
            "<code>curl http://localhost:5050/api/health</code><br/>"
            "<code>curl http://localhost:5050/api/stats</code>",
            code_style
        )]
    ]
    t_cmd = Table(cmd_box, colWidths=[7.1*inch])
    t_cmd.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94a3b8")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_cmd)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Summary & Academic Value:</b> Eye of Odin demonstrates how modern WebGL graphics, spatial 3D interaction design, lightweight native backend architectures, and intelligent affinity scoring algorithms combine to transform campus administrative utilities into engaging, secure, and user-centric student services.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF: {filename}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else "Project_Description_and_Output_Documentation.pdf"
    build_pdf(target)
