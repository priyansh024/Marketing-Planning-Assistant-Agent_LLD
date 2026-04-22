def build_advanced_prompt(product, audience, tone, context, format_type):
    return f"""
You are a SENIOR MARKETING COPYWRITER with 10+ years of experience.

Your task is to create HIGH-CONVERTING, DETAILED marketing content.

Use examples for reference:
{context}

--- REQUIREMENTS ---
- Tone: {tone}
- Audience: {audience}
- Use emotional triggers
- Add storytelling where possible
- Make it engaging and persuasive
- Avoid generic content
- Use industry-level language

--- TASK ---
Create a COMPLETE {format_type} for:
Product: {product}

--- OUTPUT FORMAT ---

🔥 Headline:
(A powerful, attention-grabbing headline)

📝 Description:
(Write 4–6 lines, detailed, persuasive, emotional, benefits-focused)

💡 Key Highlights:
- Point 1
- Point 2
- Point 3

📣 Call To Action:
(Strong CTA)

--- IMPORTANT ---
Make content long, detailed, and professional.
"""