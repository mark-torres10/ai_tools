# 🎬 Workflow: Create AI Video Prompts for Projects

## Overview
This workflow guides you through creating production-ready AI video prompts from initial brainstorming to final shot generation instructions. The process transforms freeform creative ideas into structured, executable prompts optimized for specific AI models.

## 📁 Project Folder Structure
All AI video projects follow a consistent folder structure for organization and collaboration:

```
/projects
  /creative_{project_name}
    /storyboard
      - storyboard_sketches.md
      - visual_references.md
      - shot_sequence.md
    /shots
      - shot_001_prompt.md
      - shot_002_prompt.md
      - shot_003_prompt.md
      - [additional shot files]
    creative_production_braindump.md
    INSTRUCTIONS_SHOT_GENERATION.md
    project_brief.md
    brand_guidelines.md
```

**Folder Structure Guidelines:**
- **Project Name**: Use descriptive, kebab-case naming (e.g., `creative_product_launch_video`, `creative_brand_story_campaign`)
- **Storyboard Folder**: Contains visual planning documents, sketches, and reference materials
- **Shots Folder**: Individual shot prompt files for each scene or sequence
- **Root Files**: Main project documentation and workflow files

---

## 📋 Workflow Outline

### Phase 1: Initial Brainstorming and Context Gathering
- **Objective**: Establish comprehensive understanding of project requirements, constraints, and context
- **Process**: Collaborative exploration with AI agent to capture all initial thoughts and requirements
- **Deliverable**: `creative_production_braindump.md` with structured context and questions
- **Location**: `/projects/creative_{project_name}/creative_production_braindump.md`

### Phase 2: Project Structure and Shot Planning
- **Objective**: Break down the project into discrete, manageable shots with clear narrative flow
- **Process**: Walk through each proposed shot, following the 8-Part Cinematic Framework
- **Deliverable**: Structured shot breakdown with creative vision and technical specifications
- **Location**: `/projects/creative_{project_name}/storyboard/shot_sequence.md`

### Phase 3: Prompt Development and Optimization
- **Objective**: Create model-specific prompts for each shot, optimized for target AI models
- **Process**: Apply `HOW_TO_CREATE_AI_VIDEO_PROMPTS_FOR_PROJECT.md` guidelines to each shot
- **Deliverable**: Individual shot prompts with model-specific optimizations
- **Location**: `/projects/creative_{project_name}/shots/shot_XXX_prompt.md`

### Phase 4: Audio Integration and Synchronization
- **Objective**: Develop audio scripts and synchronization instructions for each shot
- **Process**: Create dialogue, music, and sound effect specifications aligned with visual content
- **Deliverable**: Audio scripts with timing and synchronization notes
- **Location**: Integrated into individual shot files in `/projects/creative_{project_name}/shots/`

### Phase 5: Post-Production and Assembly Instructions
- **Objective**: Define how to combine video and audio elements into final deliverables
- **Process**: Create step-by-step instructions for stitching, editing, and quality assurance
- **Deliverable**: `INSTRUCTIONS_SHOT_GENERATION.md` with complete production workflow
- **Location**: `/projects/creative_{project_name}/INSTRUCTIONS_SHOT_GENERATION.md`

---

## 🎯 Success Criteria
- **Creative Vision**: Each shot aligns with overall project narrative and brand guidelines
- **Technical Quality**: Prompts optimized for specific AI models with clear success metrics
- **Production Ready**: Instructions detailed enough for immediate execution by creative teams
- **Scalable Process**: Workflow can be adapted for different project types and requirements

---

## 🚀 Project Initialization

### Setup Project Folder Structure
Before beginning any AI video project, create the standardized folder structure:

1. **Create main project folder**: `/projects/creative_{project_name}/`
2. **Create subfolders**:
   - `/storyboard/` - Visual planning and reference materials
   - `/shots/` - Individual shot prompt files
3. **Initialize root files**:
   - `creative_production_braindump.md` - Initial brainstorming document
   - `project_brief.md` - Project overview and requirements
   - `brand_guidelines.md` - Brand identity and visual requirements

### Project Naming Convention
- Use descriptive, kebab-case naming
- Include project type or purpose
- Examples: `creative_product_launch_video`, `creative_brand_story_campaign`, `creative_tutorial_series`

### File Naming Standards
- **Shot files**: `shot_001_prompt.md`, `shot_002_prompt.md`, etc.
- **Storyboard files**: `shot_sequence.md`, `visual_references.md`, `storyboard_sketches.md`
- **Project files**: `creative_production_braindump.md`, `project_brief.md`, `brand_guidelines.md`
- **Final deliverable**: `INSTRUCTIONS_SHOT_GENERATION.md`

### File Organization Guidelines
- **Keep related files together** in appropriate subfolders
- **Use consistent naming** across all project files
- **Include version numbers** for major revisions (e.g., `shot_001_prompt_v2.md`)
- **Maintain clear file hierarchy** for easy navigation and collaboration

---

## Phase 1: Initial Brainstorming and Context Gathering

### Objective
Establish a comprehensive understanding of the project requirements, constraints, and context through collaborative exploration with an AI agent.

### Process

#### 1.1 Initiate Brainstorming Session
- **Engage with AI agent** to explore the project concept in freeform discussion
- **Capture all initial thoughts**, requirements, and creative ideas
- **Document existing constraints**, deadlines, and stakeholder requirements
- **Identify target audience** and use case scenarios

#### 1.2 Context Gathering Questions
The AI agent should ask comprehensive questions based on the 8-Part Cinematic Framework:

**Project Context & Brand Alignment:**
- What is the project's primary purpose and business objective?
- Who is the target audience and what are their characteristics?
- What are the brand guidelines, visual identity, and messaging requirements?
- What is the project timeline and budget constraints?
- Are there any existing creative briefs or reference materials?

**Creative Vision & Narrative:**
- What story or message do you want to communicate?
- What is the overall tone and emotional impact you're seeking?
- Are there specific visual metaphors or symbolic elements?
- What is the desired length and format of the final video?
- Are there any specific scenes or moments that must be included?

**Technical Requirements:**
- Which AI video generation model(s) will you be using?
- What are the technical specifications (resolution, aspect ratio, duration)?
- Are there specific camera styles or cinematographic approaches?
- What audio requirements do you have (music, dialogue, sound effects)?
- Are there any post-production or editing requirements?

**Character & Setting:**
- Who are the main subjects or characters in the video?
- What are their key characteristics and visual appearance?
- Where does the action take place (specific locations, environments)?
- What is the time period or era of the setting?
- Are there any specific props, objects, or visual elements?

**Lighting & Mood:**
- What is the desired lighting style and mood?
- What time of day or atmospheric conditions?
- Are there specific color palettes or visual themes?
- What emotional tone should the lighting convey?

**Audio Design:**
- What type of audio do you need (dialogue, music, ambient sounds)?
- Are there specific audio cues or timing requirements?
- Do you need synchronized audio with visual elements?
- What is the desired audio quality and style?

#### 1.3 Create Brain Dump File
- **Generate `creative_production_braindump.md`** to capture all unstructured thoughts and context
- **Include questions that need answers**, potential risks, and initial scope ideas
- **Document any existing research**, similar projects, or relevant background information
- **Structure the information** using the 8-Part Cinematic Framework as a guide

#### 1.4 Identify Knowledge Gaps
- **List areas requiring further clarification** or research
- **Note dependencies** on external stakeholders or systems
- **Flag potential technical or business risks** that need investigation
- **Identify missing brand assets** or reference materials

### Deliverables
- **`/projects/creative_{project_name}/creative_production_braindump.md`** containing all initial thoughts and context
- **`/projects/creative_{project_name}/project_brief.md`** with project overview and requirements
- **`/projects/creative_{project_name}/brand_guidelines.md`** with brand identity and visual requirements
- **List of questions requiring answers** from stakeholders
- **Initial scope boundaries and constraints** identified
- **Knowledge gaps** that need to be addressed before proceeding

### Success Criteria
- **Comprehensive context captured** across all 8-Part Cinematic Framework elements
- **Clear project objectives** and constraints documented
- **Target audience and use cases** clearly defined
- **Technical requirements** and AI model preferences specified
- **Brand alignment** and visual identity requirements established

### Next Steps
After completing Phase 1, present the `creative_production_braindump.md` for approval before proceeding to Phase 2: Project Structure and Shot Planning.

---

## Phase 2: Project Structure and Shot Planning

### Objective
Break down the project into discrete, manageable shots with clear narrative flow, ensuring each shot serves the overall creative vision and can be executed effectively with AI video generation tools.

### Process

#### 2.1 Analyze Brain Dump and Extract Key Elements
- **Review `creative_production_braindump.md`** to identify core narrative elements
- **Extract main story beats** and emotional progression
- **Identify key visual moments** that must be captured
- **Map out character arcs** and visual development
- **Define scene transitions** and continuity requirements

#### 2.2 Create Shot Breakdown Structure
- **Define total number of shots** based on project length and complexity
- **Establish shot sequence** following narrative logic
- **Assign approximate duration** for each shot (typically 3-8 seconds per shot)
- **Identify shot types** (establishing, medium, close-up, etc.)
- **Plan visual continuity** between shots

#### 2.3 Walk Through Each Proposed Shot
For each shot, systematically apply the 8-Part Cinematic Framework:

**Scene Description (Core Action):**
- What is the primary action happening in this shot?
- What is the emotional context and purpose?
- How does this shot advance the overall narrative?

**Visual Style (Aesthetic Direction):**
- What cinematic approach best serves this shot?
- What visual style aligns with brand guidelines?
- Are there specific film references or inspirations?

**Camera Movement (Dynamic Direction):**
- What camera behavior best captures this moment?
- How does camera movement serve the narrative?
- What technical specifications are needed?

**Main Subject (Character Focus):**
- Who or what is the primary focus of this shot?
- What are their specific characteristics and appearance?
- What actions or expressions are they performing?

**Background Setting (Environmental Context):**
- Where does this shot take place?
- What environmental details support the narrative?
- What atmospheric elements enhance the mood?

**Lighting and Mood (Emotional Tone):**
- What lighting setup creates the desired mood?
- What time of day or atmospheric conditions?
- How does lighting support the emotional impact?

**Audio Cue (Sonic Landscape):**
- What audio elements are needed for this shot?
- How does audio support the visual narrative?
- What timing and synchronization requirements exist?

**Color Palette (Visual Harmony):**
- What color scheme supports the shot's purpose?
- How does color enhance the emotional impact?
- What brand color requirements must be maintained?

#### 2.4 Validate Shot Sequence
- **Review narrative flow** to ensure logical progression
- **Check visual continuity** between consecutive shots
- **Validate technical feasibility** for each shot
- **Confirm brand alignment** across all shots
- **Assess resource requirements** and constraints

#### 2.5 Create Shot Planning Document
- **Generate structured shot breakdown** with all 8-Part Framework elements
- **Include shot timing** and transition notes
- **Document technical requirements** for each shot
- **Note dependencies** between shots
- **Flag potential challenges** or risks

### Deliverables
- **`/projects/creative_{project_name}/storyboard/shot_sequence.md`** with structured shot breakdown and 8-Part Cinematic Framework
- **`/projects/creative_{project_name}/storyboard/visual_references.md`** with reference materials and inspiration
- **Shot sequence timeline** with durations and transitions
- **Technical requirements summary** for each shot
- **Visual continuity notes** between shots
- **Risk assessment** and mitigation strategies

### Success Criteria
- **Clear narrative progression** through all shots
- **Each shot serves a specific purpose** in the overall story
- **Technical feasibility** confirmed for all proposed shots
- **Brand consistency** maintained across all shots
- **Visual continuity** planned between consecutive shots

### Next Steps
After completing Phase 2, present the shot breakdown for approval before proceeding to Phase 3: Prompt Development and Optimization.

---

## Phase 3: Prompt Development and Optimization

### Objective
Create model-specific prompts for each shot, optimized for target AI models, following the guidelines from `HOW_TO_CREATE_AI_VIDEO_PROMPTS_FOR_PROJECT.md` and `WHAT_MAKES_A_GOOD_AI_VIDEO_PROMPT.md`.

### Process

#### 3.1 Review Shot Planning and Model Selection
- **Analyze shot breakdown** from Phase 2
- **Confirm target AI model(s)** for each shot (Veo3, Runway Gen-4, Luma Dream Machine, Pika 1.5)
- **Identify model-specific capabilities** that should be leveraged
- **Note any model limitations** that need to be worked around
- **Plan prompt optimization strategy** for each model

#### 3.2 Develop Individual Shot Prompts
For each shot, create a comprehensive prompt following the 8-Part Cinematic Framework:

**3.2.1 Apply Project Context & Brand Alignment**
- Integrate brand guidelines and visual identity
- Ensure target audience alignment
- Include business objectives and messaging
- Reference brand color palettes and style requirements

**3.2.2 Craft Creative Vision & Narrative**
- Define clear story arc for the shot
- Establish emotional tone and impact
- Include visual metaphors and symbolic elements
- Ensure narrative continuity with other shots

**3.2.3 Specify Technical Requirements**
- Define camera work (shot types, movements, compositions)
- Specify lighting setup and color temperature
- Include audio design requirements
- Note post-production considerations

**3.2.4 Detail Character & Setting Elements**
- Describe main subjects with specific characteristics
- Define environmental context and world-building
- Include props, objects, and visual elements
- Specify scale and perspective choices

**3.2.5 Optimize for Target AI Model**
Apply model-specific optimization strategies:

**For Veo3:**
- Leverage native audio generation capabilities
- Use image-to-video features for character consistency
- Focus on physics and realistic movement
- Include rich detail (60-100 words)

**For Runway Gen-4:**
- Start with simple, clear prompts
- Use keyframe functionality for character consistency
- Focus on visual references and high-quality images
- Build complexity gradually

**For Luma Dream Machine:**
- Use natural, conversational language
- Leverage character reference system
- Focus on cinematic movements and natural motion
- Include emotional context and atmosphere

**For Pika 1.5:**
- Utilize motion effects and dynamic movement
- Leverage lip sync capabilities for dialogue
- Use video-to-video transformation features
- Focus on motion and visual effects

#### 3.3 Validate and Refine Prompts
- **Test prompt clarity** and specificity
- **Verify model compatibility** and optimization
- **Check brand alignment** and consistency
- **Ensure technical feasibility** and accuracy
- **Validate narrative coherence** with other shots

#### 3.4 Create Prompt Documentation
- **Document each shot prompt** with full 8-Part Framework
- **Include model-specific optimizations** and rationale
- **Note success criteria** and evaluation metrics
- **Document potential variations** or alternatives
- **Include troubleshooting notes** and common issues

#### 3.5 Quality Assurance Review
- **Review all prompts** for consistency and quality
- **Validate brand alignment** across all shots
- **Check technical accuracy** and feasibility
- **Ensure narrative flow** and continuity
- **Test model-specific optimizations**

### Deliverables
- **Individual shot prompt files** in `/projects/creative_{project_name}/shots/shot_XXX_prompt.md`
- **Model-specific optimization notes** and rationale for each shot
- **Success criteria** and evaluation metrics for each shot
- **Troubleshooting guide** for common issues
- **Prompt variations** and alternatives where applicable

### Success Criteria
- **Each prompt follows** the 8-Part Cinematic Framework completely
- **Model-specific optimizations** are properly applied
- **Brand guidelines** are consistently integrated
- **Technical specifications** are accurate and feasible
- **Narrative coherence** is maintained across all shots

### Next Steps
After completing Phase 3, present the individual shot prompts for approval before proceeding to Phase 4: Audio Integration and Synchronization.

---

## Phase 4: Audio Integration and Synchronization

### Objective
Develop audio scripts and synchronization instructions for each shot, ensuring seamless integration between visual and audio elements while maintaining brand voice and narrative coherence.

### Process

#### 4.1 Review Shot Prompts and Audio Requirements
- **Analyze individual shot prompts** from Phase 3
- **Identify audio requirements** for each shot (dialogue, music, sound effects, ambient)
- **Review brand voice guidelines** and messaging requirements
- **Assess audio synchronization needs** with visual elements
- **Plan audio model selection** (text-to-speech, music generation, sound effects)

#### 4.2 Develop Audio Scripts for Each Shot
For each shot, create comprehensive audio specifications:

**4.2.1 Dialogue and Voice-Over Scripts**
- **Write clear, natural dialogue** that serves the narrative
- **Include character voice descriptions** (tone, pace, emotion)
- **Specify timing and pacing** for delivery
- **Note pronunciation guides** for technical terms or brand names
- **Include emotional context** and delivery instructions

**4.2.2 Music and Soundtrack Specifications**
- **Define musical style and mood** for each shot
- **Specify tempo and rhythm** requirements
- **Include instrumentation preferences** and arrangements
- **Note volume and mixing requirements**
- **Plan musical transitions** between shots

**4.2.3 Sound Effects and Ambient Audio**
- **Identify specific sound effects** needed for each shot
- **Define ambient soundscapes** and environmental audio
- **Specify audio quality and realism** requirements
- **Note timing and synchronization** with visual elements
- **Include audio layering** and mixing instructions

**4.2.4 Audio Timing and Synchronization**
- **Define precise timing** for audio elements
- **Specify synchronization points** with visual actions
- **Plan audio transitions** between shots
- **Note fade-in/fade-out requirements**
- **Include audio cue timing** for visual elements

#### 4.3 Optimize Audio for Target Models
Apply model-specific audio optimization strategies:

**For Veo3 (Native Audio Generation):**
- Leverage built-in audio generation capabilities
- Use natural language descriptions for audio
- Focus on synchronized audio with visual elements
- Include specific dialogue and sound effect descriptions

**For External Text-to-Speech Models:**
- Write clear, natural dialogue scripts
- Include pronunciation guides and emphasis
- Specify voice characteristics and emotional tone
- Plan timing and pacing for delivery

**For Music Generation Models:**
- Use descriptive musical language
- Specify style, mood, and instrumentation
- Include tempo and rhythm requirements
- Plan musical structure and progression

**For Sound Effects Libraries:**
- Identify specific sound effect requirements
- Note quality and realism standards
- Plan layering and mixing approaches
- Include timing and synchronization notes

#### 4.4 Create Audio Production Instructions
- **Document audio generation process** for each shot
- **Include model-specific instructions** and parameters
- **Note quality control measures** and evaluation criteria
- **Plan audio editing and mixing** requirements
- **Include troubleshooting guides** for common audio issues

#### 4.5 Validate Audio Integration
- **Review audio scripts** for narrative coherence
- **Check brand voice alignment** across all shots
- **Validate timing and synchronization** requirements
- **Ensure audio quality standards** are met
- **Test audio model compatibility** and capabilities

### Deliverables
- **Audio scripts integrated** into individual shot files in `/projects/creative_{project_name}/shots/`
- **Audio timing and synchronization** specifications for each shot
- **Model-specific audio generation** instructions
- **Audio production workflow** and quality control measures
- **Troubleshooting guide** for audio generation issues

### Success Criteria
- **Audio scripts align** with visual content and narrative flow
- **Brand voice consistency** maintained across all dialogue
- **Audio timing and synchronization** properly specified
- **Model-specific optimizations** correctly applied
- **Quality standards** defined and achievable

### Next Steps
After completing Phase 4, present the audio integration specifications for approval before proceeding to Phase 5: Post-Production and Assembly Instructions.

---

## Phase 5: Post-Production and Assembly Instructions

### Objective
Create the final `INSTRUCTIONS_SHOT_GENERATION.md` file with comprehensive production workflow, including detailed instructions for video generation, audio integration, post-processing, and quality assurance.

### Process

#### 5.1 Compile All Previous Phase Deliverables
- **Review shot breakdown** from Phase 2
- **Consolidate individual shot prompts** from Phase 3
- **Integrate audio scripts and specifications** from Phase 4
- **Organize model-specific optimizations** and requirements
- **Validate completeness** of all components

#### 5.2 Create Shot-by-Shot Generation Instructions
For each shot, create comprehensive instructions following this structure:

**5.2.1 Shot Overview and Context**
- **Shot number and title**
- **Duration and timing** within overall project
- **Narrative purpose** and story function
- **Visual continuity notes** with previous/next shots
- **Brand alignment** and messaging requirements

**5.2.2 Instructions for Video Model**
- **Complete AI video prompt** optimized for target model
- **Model-specific parameters** and settings
- **Reference images or assets** to upload
- **Generation settings** (resolution, duration, quality)
- **Success evaluation criteria** and quality metrics
- **Common issues** and troubleshooting notes

**5.2.3 Instructions for Audio Model**
- **Complete audio script** with dialogue, music, and sound effects
- **Audio model parameters** and voice settings
- **Timing and synchronization** requirements
- **Audio quality standards** and evaluation criteria
- **Common audio issues** and troubleshooting notes

**5.2.4 Post-Processing Instructions**
- **Video editing requirements** (trimming, color correction, effects)
- **Audio editing and mixing** specifications
- **Synchronization process** between video and audio
- **Quality control checks** and validation steps
- **File format and export** requirements

#### 5.3 Create Overall Project Assembly Instructions
- **Shot sequence and timing** for final assembly
- **Transition effects** between shots
- **Overall audio mixing** and mastering
- **Color grading consistency** across all shots
- **Final export specifications** and delivery requirements

#### 5.4 Develop Quality Assurance Framework
- **Pre-generation checklist** for each shot
- **Post-generation validation** criteria
- **Quality control checkpoints** throughout process
- **Revision and iteration** procedures
- **Final approval process** and sign-off requirements

#### 5.5 Create Troubleshooting and Support Documentation
- **Common issues** and solutions for each AI model
- **Technical troubleshooting** guides
- **Quality control** procedures and checklists
- **Escalation procedures** for complex issues
- **Resource requirements** and dependencies

### Deliverables
- **`/projects/creative_{project_name}/INSTRUCTIONS_SHOT_GENERATION.md`** - Complete production workflow document
- **Individual shot instructions** with video and audio generation details
- **Post-processing workflow** and assembly instructions
- **Quality assurance framework** and validation procedures
- **Troubleshooting guides** and support documentation

### Final Document Structure
The `INSTRUCTIONS_SHOT_GENERATION.md` file will include:

```
# Instructions for Shot Generation

## Project Overview
- Project context and objectives
- Brand guidelines and requirements
- Target audience and use cases
- Technical specifications and constraints

## Shot Outline
- Complete shot sequence with timing
- Narrative flow and transitions
- Visual continuity notes
- Audio synchronization points

## Shot 1: [Shot Title]
### Instructions for Video Model
- Complete AI video prompt
- Model-specific parameters and settings
- Reference assets and uploads
- Success evaluation criteria
- Common issues and troubleshooting

### Instructions for Audio Model
- Complete audio script
- Audio model parameters and settings
- Timing and synchronization requirements
- Audio quality standards
- Common issues and troubleshooting

### Post-Processing Instructions
- Video editing requirements
- Audio editing and mixing
- Synchronization process
- Quality control checks
- File format and export

## Shot 2: [Shot Title]
[Same structure as Shot 1]

## Shot N: [Shot Title]
[Same structure as Shot 1]

## Final Assembly
- Shot sequence and timing
- Transition effects
- Overall audio mixing
- Color grading consistency
- Final export specifications

## Quality Assurance
- Pre-generation checklist
- Post-generation validation
- Quality control checkpoints
- Revision procedures
- Final approval process

## Troubleshooting
- Common issues and solutions
- Technical troubleshooting guides
- Quality control procedures
- Escalation procedures
- Resource requirements

## Final Deliverables
- Video files and specifications
- Audio files and specifications
- Project documentation
- Quality assurance reports
- Delivery confirmation
```

### Success Criteria
- **Complete production workflow** documented and ready for execution
- **All shot instructions** include video and audio generation details
- **Post-processing procedures** clearly defined and actionable
- **Quality assurance framework** ensures consistent output quality
- **Troubleshooting guides** address common issues and challenges

### Final Review and Approval
After completing Phase 5, present the complete `INSTRUCTIONS_SHOT_GENERATION.md` file for final approval. This document will serve as the comprehensive production guide for executing the entire AI video project.

---

*This workflow ensures systematic transformation of creative ideas into production-ready AI video content while maintaining quality, consistency, and brand alignment throughout the process.*
