from io import BytesIO

from reportlab.lib import colors

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)

from reportlab.lib.enums import (
    TA_CENTER,
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
)
# ---------- COLORS ----------

BACKGROUND = colors.HexColor("#0F172A")

CARD = colors.HexColor("#1E293B")

PRIMARY = colors.HexColor("#3B82F6")

SUCCESS = colors.HexColor("#22C55E")

TEXT = colors.HexColor("#FFFFFF")

MUTED = colors.HexColor("#94A3B8")


def create_kpi_card(
    title,
    value,
    bg_color
):
    data = [
        [
            Paragraph(
                f"""
                <para align='center'>
                <font size='18'>
                <b>{value}</b>
                </font>
                <br/>
                <font size='10'>
                {title}
                </font>
                </para>
                """
            )
        ]
    ]

    table = Table(
        data,
        colWidths=150,
        rowHeights=80,
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    bg_color,
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, -1),
                    colors.white,
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    bg_color,
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
            ]
        )
    )

    return table


def create_info_card(
    title,
    content,
    bg_color=colors.whitesmoke
):

    table = Table(
        [
            [
                Paragraph(
                    f"<b>{title}</b>"
                )
            ],

            [
                Paragraph(
                    content
                )
            ]
        ],
        colWidths=500
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    bg_color
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    12
                ),

                (
                    "TOPPADDING",
                    (0, 1),
                    (-1, -1),
                    10
                )
            ]
        )
    )

    return table


def create_content_card(
    title,
    content,
    bg_color=colors.whitesmoke
):

    table = Table(
        [
            [
                Paragraph(
                    f"<b>{title}</b>"
                )
            ],

            [
                Paragraph(
                    content
                )
            ]
        ],
        colWidths=500
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    bg_color
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10
                ),

                (
                    "TOPPADDING",
                    (0, 1),
                    (-1, -1),
                    12
                ),

                (
                    "BOTTOMPADDING",
                    (0, 1),
                    (-1, -1),
                    12
                )
            ]
        )
    )

    return table

def create_timeline_block(
    title,
    content,
    color
):

    table = Table(
        [
            [
                Paragraph(
                    f"<b>{title}</b>"
                )
            ],

            [
                Paragraph(
                    content
                )
            ]
        ],
        colWidths=500
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    color
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10
                )
            ]
        )
    )

    return table


def generate_sales_report(
    report_data: dict
):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []

    # ==========================
    # CUSTOM STYLES
    # ==========================

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        textColor=TEXT,
        alignment=TA_CENTER,
        fontSize=28,
        leading=32,
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        textColor=MUTED,
        alignment=TA_CENTER,
        fontSize=12,
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        textColor=PRIMARY,
        fontSize=18,
        spaceAfter=12,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=11,
        leading=18,
    )

    # ==========================
    # PREMIUM COVER PAGE
    # ==========================

    story.append(
        Spacer(1, 120)
    )

    story.append(
        Paragraph(
            """
            <para align='center'>
            <font size='34'>
            <b>ScaleSDR</b>
            </font>
            </para>
            
            """,
            styles["Normal"],
        )
    )

    story.append(
        Spacer(1, 15)
    )

    story.append(
        Paragraph(
            """
            <para align='center'>
            <font size='18'>
            Human-grade outreach at machine-scale.
            </font>
            </para>
            """,
            styles["Normal"],
        )
    )

    story.append(
        Spacer(1, 60)
    )

    company_name = report_data[
        "company_analysis"
    ].get(
        "company_name",
        "Unknown Company"
    )

    story.append(
        Paragraph(
            f"""
            <para align='center'>
            <font size='28'>
            <b>{company_name}</b>
            </font>
            </para>
            """,
            styles["Normal"],
        )
    )

    story.append(
        Spacer(1, 40)
    )

    score = report_data[
        "lead_score"
    ].get(
        "score",
        0
    )

    qualification = report_data[
        "lead_score"
    ].get(
        "qualification",
        "Unknown"
    )

    story.append(
        create_kpi_card(
            "Lead Score",
            f"{score}/100",
            PRIMARY,
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        create_kpi_card(
            "Qualification",
            qualification,
            SUCCESS,
        )
    )

    story.append(
        Spacer(1, 50)
    )

    story.append(
        Paragraph(
            """
            <para align='center'>
            Generated by Multi-Agent AI Workflow
            </para>
            """,
            styles["Normal"],
        )
    )

    story.append(
        PageBreak()
    )
    # ==========================
    # EXECUTIVE SUMMARY
    # ==========================

    story.append(
    Paragraph(
        "Executive Summary",
        section_style
    )
)

    story.append(
        Spacer(1, 20)
    )

    industry = report_data[
        "company_analysis"
    ].get(
        "industry",
        "Unknown"
    )

    score = report_data[
        "lead_score"
    ].get(
        "score",
        0
    )

    qualification = report_data[
        "lead_score"
    ].get(
        "qualification",
        "Unknown"
    )

    kpi_table = Table(
        [
            [
                create_kpi_card(
                    "Lead Score",
                    score,
                    PRIMARY,
                ),

                create_kpi_card(
                    "Industry",
                    industry,
                    colors.HexColor(
                        "#8B5CF6"
                    ),
                ),

                create_kpi_card(
                    "Status",
                    qualification,
                    SUCCESS,
                ),
            ]
        ]
    )

    story.append(
        kpi_table
    )

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            """
            This report contains AI-generated
            company intelligence, pain point
            analysis, lead qualification,
            outreach recommendations and
            competitive positioning insights.
            """,
            body_style
        )
    )

    story.append(
        PageBreak()
    )

    # ==========================
    # COMPANY ANALYSIS
    # ==========================

    story.append(
    Paragraph(
        "Company Analysis",
        section_style
    )
)

    story.append(
        Spacer(1, 20)
    )

    company = report_data[
        "company_analysis"
    ]

    company_table = Table(
        [
            [
                "Industry",
                company.get(
                    "industry",
                    "N/A"
                ),
            ],

            [
                "Business Model",
                company.get(
                    "business_model",
                    "N/A"
                ),
            ],
        ],
        colWidths=[140, 320]
    )

    company_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.whitesmoke,
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey,
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold",
                ),
            ]
        )
    )

    story.append(
        company_table
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "<b>Company Summary</b>",
            body_style
        )
    )

    story.append(
        Paragraph(
            company.get(
                "company_summary",
                ""
            ),
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "<b>Main Services</b>",
            body_style
        )
    )

    services = company.get(
        "main_services",
        []
    )

    service_text = "<br/>".join(
        [
            f"• {s}"
            for s in services
        ]
    )

    story.append(
        Paragraph(
            service_text,
            body_style
        )
    )

    story.append(
        PageBreak()
    )


    # ==========================
    # COMPETITOR INTELLIGENCE
    # ==========================

    competitor_data = report_data.get(
        "competitor_analysis"
    )

    if competitor_data:

        story.append(
            Paragraph(
                "Competitor Intelligence",
                section_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        company_name = report_data[
            "company_analysis"
        ].get(
            "company_name",
            "Target Company"
        )

        competitor_name = (
            competitor_data.get(
                "main_competitor",
                "Unknown"
            )
        )

        comparison_table = Table(
            [
                [
                    Paragraph(
                        f"<b>{company_name}</b>"
                    ),

                    Paragraph(
                        "<b>VS</b>"
                    ),

                    Paragraph(
                        f"<b>{competitor_name}</b>"
                    ),
                ]
            ],
            colWidths=[
                200,
                60,
                200
            ]
        )

        comparison_table.setStyle(
            TableStyle(
                [
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),

                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, 0),
                        PRIMARY
                    ),

                    (
                        "BACKGROUND",
                        (2, 0),
                        (2, 0),
                        colors.HexColor(
                            "#EF4444"
                        )
                    ),

                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, -1),
                        colors.white
                    ),
                ]
            )
        )

        story.append(
            comparison_table
        )

        story.append(
            Spacer(1, 20)
        )

        weaknesses = "<br/>".join(
            [
                f"• {item}"
                for item in competitor_data.get(
                    "competitor_weaknesses",
                    []
                )
            ]
        )

        story.append(
            create_info_card(
                "Competitor Weaknesses",
                weaknesses,
                colors.HexColor(
                    "#FEE2E2"
                )
            )
        )

        story.append(
            Spacer(1, 12)
        )

        pricing = "<br/>".join(
            [
                f"• {item}"
                for item in competitor_data.get(
                    "pricing_gaps",
                    []
                )
            ]
        )

        story.append(
            create_info_card(
                "Pricing Gaps",
                pricing,
                colors.HexColor(
                    "#FEF3C7"
                )
            )
        )

        story.append(
            Spacer(1, 12)
        )

        story.append(
            create_info_card(
                "Sales Wedge",
                competitor_data.get(
                    "sales_wedge",
                    ""
                ),
                colors.HexColor(
                    "#DCFCE7"
                )
            )
        )

        story.append(
            Spacer(1, 12)
        )

        story.append(
            create_info_card(
                "Recommended Pitch",
                competitor_data.get(
                    "recommended_pitch",
                    ""
                ),
                colors.HexColor(
                    "#DBEAFE"
                )
            )
        )

        story.append(
            PageBreak()
        )

    
    # ==========================
    # PAIN POINT ANALYSIS
    # ==========================

    pain_data = report_data.get(
        "pain_points"
    )

    if pain_data:

        story.append(
            Paragraph(
                "Pain Point Analysis",
                section_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        for pain_point in pain_data.get(
            "pain_points",
            []
        ):

            story.append(
                create_info_card(
                    "Pain Point",
                    pain_point,
                    colors.HexColor(
                        "#FEE2E2"
                    )
                )
            )

            story.append(
                Spacer(1, 10)
            )

        story.append(
            PageBreak()
        )


    # ==========================
    # OUTREACH ASSETS
    # ==========================

    outreach = report_data.get(
        "outreach"
    )

    if outreach:

        story.append(
            Paragraph(
                "Outreach Assets",
                section_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            create_content_card(
                "Email Subject",
                outreach.get(
                    "email_subject",
                    ""
                ),
                colors.HexColor(
                    "#DBEAFE"
                )
            )
        )

        story.append(
            Spacer(1, 12)
        )

        story.append(
            create_content_card(
                "Email Body",
                outreach.get(
                    "email_body",
                    ""
                ),
                colors.HexColor(
                    "#DCFCE7"
                )
            )
        )

        story.append(
            Spacer(1, 12)
        )

        story.append(
            create_content_card(
                "LinkedIn Message",
                outreach.get(
                    "linkedin_message",
                    ""
                ),
                colors.HexColor(
                    "#EDE9FE"
                )
            )
        )

        story.append(
            PageBreak()
        )



    # ==========================
    # FOLLOW-UP STRATEGY
    # ==========================

    followups = report_data.get(
        "followups"
    )

    if followups:

        story.append(
            Paragraph(
                "Follow-Up Strategy",
                section_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            Paragraph(
                """
                Recommended Follow-Up Journey
                """,
                body_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        day3 = followups.get(
            "day3"
        )

        if day3:

            story.append(
                create_timeline_block(
                    "Day 3 Follow-Up",
                    day3.get(
                        "email_body",
                        ""
                    ),
                    colors.HexColor(
                        "#DBEAFE"
                    )
                )
            )

            story.append(
                Spacer(1, 10)
            )

        day7 = followups.get(
            "day7"
        )

        if day7:

            story.append(
                create_timeline_block(
                    "Day 7 Follow-Up",
                    day7.get(
                        "email_body",
                        ""
                    ),
                    colors.HexColor(
                        "#DCFCE7"
                    )
                )
            )

            story.append(
                Spacer(1, 10)
            )

        breakup = followups.get(
            "breakup"
        )

        if breakup:

            story.append(
                create_timeline_block(
                    "Final Breakup Email",
                    breakup.get(
                        "email_body",
                        ""
                    ),
                    colors.HexColor(
                        "#FEE2E2"
                    )
                )
            )

        story.append(
            PageBreak()
        )

    # ==========================
    # AGENT EXECUTION SUMMARY
    # ==========================

    story.append(
        Paragraph(
            "Agent Execution Summary",
            section_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    agents_table = Table(
        [
            ["✓", "Research Agent"],
            ["✓", "Pain Point Agent"],
            ["✓", "Lead Score Agent"],
            ["✓", "Outreach Agent"],
            ["✓", "Competitor Agent"],
            ["✓", "Follow-Up Agent"],
        ],
        colWidths=[
            50,
            400
        ]
    )

    agents_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.whitesmoke
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, -1),
                    "Helvetica-Bold"
                )
            ]
        )
    )

    story.append(
        agents_table
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            """
            This report was generated using a
            coordinated multi-agent workflow
            combining research, lead scoring,
            outreach generation, competitor
            intelligence, and follow-up planning.
            """,
            body_style
        )
    )


    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf