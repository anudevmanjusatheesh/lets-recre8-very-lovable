#!/usr/bin/env python
import sys
from build_anything.crew import BuildAnythingCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    
    taskExp = """Create a highly immersive, single-page portfolio website for an AI  company Synbrains Solutions provate limited. The website should feature stunning 3D animations, smooth interactions, and a futuristic aesthetic. It should include a dynamic navigation system, scrolling effects, animated 3D elements, interactive sections, and fluid transitions. The site must feel cutting-edge and modern, conveying technological advancement and AI innovation."

    🌐 Website Features
    🖥️ 1. Hero Section (Landing Page)
    💡 Goal: Futuristic 3D animated hero section that immediately grabs attention.

    ✅ Background:

    Full-screen immersive 3D AI-generated digital world
    Floating particles and holographic lines animated with Three.js
    Subtle parallax depth effect when moving the cursor
    ✅ Headline (Editable Placeholder):
    "Your AI & Cybersecurity Partner for the Future."

    ✅ Animated Elements:

    Neon-glowing AI circuits forming dynamically
    3D rotating globe with connected neural networks (representing AI security infrastructure)
    Subtle glow and motion effects
    ✅ Call to Action (CTA):

    "Explore Our Work" (Smooth scroll to the next section)
    Interactive floating button with hover distortions
    🔧 2. AI & Tech Stack (What We Use)
    💡 Goal: Showcase expertise in AI, cybersecurity, and development tools in an engaging 3D format.

    ✅ Layout:

    Interactive rotating 3D hexagonal grid (Each hexagon representing a technology)
    Hover effect: Clicking a hexagon reveals more details about that tech
    Neon-glow effects with dynamic animation on hover
    ✅ Example Stacks (Editable Placeholders):
    🧠 AI & ML: [Tech 1], [Tech 2], [Tech 3] (with logos : add llamaindex, langchain, n8n, and few more AI things)
    🛠️ API Development: [Backend Framework 1], [Gateway Tool] (add kong, fastapi, flaskapi, express)

    🌍 3. Community Projects (Interactive Cards)
    💡 Goal: Highlight community-driven AI projects in an engaging way.

    ✅ Dynamic Layout:

    3D flipping cards with project previews
    Hover: Cards expand slightly with a glowing border
    Smooth scrolling on horizontal carousel format
    ✅ Example Project Placeholders:

    "Project 1" – AI-Powered Learning System
    "Project 2" – Open Source Cybersecurity AI
    🏢 4. Client Projects (Case Study Showcase)
    💡 Goal: Showcase real-world impact in an engaging format.

    ✅ Animated Section:

    3D carousel effect with real client work showcased
    Background video playing subtly (blurred effect for a futuristic feel)
    ✅ Interactive Experience:

    Hovering over a project expands it
    Auto-scroll effect for seamless transitions
    ✅ Example Placeholder Projects:

    "Client 1 – AI-Powered Fraud Detection"
    "Client 2 – API Security Enhancement"
    🚀 5. Our Products
    💡 Goal: Highlight AI-powered solutions in a dynamic format.

    ✅ 3D Scroll Interaction:

    Products appear as glowing floating cards on scroll
    Interactive mouse movement effect
    ✅ Example Placeholder Products:

    "AI Chatbot for Websites"
    "Cybersecurity AI Tool"
    🔬 6. Proof of Concepts (PoCs)
    💡 Goal: Display innovative AI PoCs with interactive elements.

    ✅ 3D Particle Effects:

    Particles forming AI-related structures as user scrolls
    Click to reveal detailed PoC descriptions
    ✅ Example Placeholder PoCs:

    "Vector Search for Legal Docs"
    "Multi-Agent AI for Cybersecurity"
    📝 7. Blog & External Links
    💡 Goal: Provide access to thought leadership content.

    ✅ Scrolling News Ticker Animation:

    Latest blog posts dynamically scrolling with glowing effects
    Auto-hover effect for instant read mode
    ✅ Example Placeholder Blog Titles:

    "How AI is Revolutionizing Cybersecurity"
    "The Future of API Security with AI"
    📞 8. Contact & CTA (Final Section)
    💡 Goal: Encourage business inquiries and engagement.

    ✅ Animated CTA:

    "Let's Build the Future Together."
    Neon-glowing "Contact Us" button with hover wave effect. There should only be a single page. No sub routes. (contact should route to https://synrbains.ai/contact"""
    
    
    inputs = {
        'user_requirement': taskExp
    }
    BuildAnythingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BuildAnythingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BuildAnythingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BuildAnythingCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
