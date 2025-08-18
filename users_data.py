from werkzeug.security import generate_password_hash

users = [
    {
        "name": "amelia",
        "description": (
            "I’m a public health advocate focused on improving maternal care in rural areas. "
            "I work closely with local clinics to provide education and resources for new mothers. "
            "My passion lies in reducing infant mortality through community outreach and support groups."
        ),
        "goals": [
            "Create educational workshops for prenatal care",
            "Develop a mobile health app for rural mothers",
            "Partner with NGOs to fund maternal health programs"
        ],
        "email": "amelia@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "brandon",
        "description": (
            "I’m a software developer with a love for open-source projects and community building. "
            "I contribute to several projects aimed at increasing accessibility in tech. "
            "When I’m not coding, I mentor aspiring programmers from underrepresented backgrounds."
        ),
        "goals": [
            "Launch a mentorship platform for coders",
            "Build accessible UI components for open-source projects",
            "Host community coding bootcamps"
        ],
        "email": "brandon@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "carmen",
        "description": (
            "As a climate scientist, I study the effects of deforestation on local ecosystems. "
            "I collaborate with activists to create awareness campaigns and push for policy change. "
            "I’m passionate about integrating traditional knowledge with modern science for conservation."
        ),
        "goals": [
            "Publish research on deforestation impacts",
            "Organize community reforestation projects",
            "Advocate for sustainable land management policies"
        ],
        "email": "carmen@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "derek",
        "description": (
            "I’m a digital artist exploring the intersection of technology and human emotion. "
            "My work focuses on immersive experiences that challenge perceptions of reality. "
            "I often collaborate with musicians and programmers to create multi-sensory installations."
        ),
        "goals": [
            "Create an interactive VR art exhibit",
            "Collaborate on a generative music project",
            "Develop workshops on digital art techniques"
        ],
        "email": "derek@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "elaine",
        "description": (
            "I’m an urban planner dedicated to creating inclusive public spaces that foster community. "
            "My projects prioritize accessibility, green spaces, and cultural heritage preservation. "
            "I believe in engaging residents through participatory design processes."
        ),
        "goals": [
            "Design a community park with local input",
            "Implement accessible transit solutions",
            "Host urban design workshops for youth"
        ],
        "email": "elaine@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "farid",
        "description": (
            "I’m a social entrepreneur working to provide clean water solutions in underserved regions. "
            "I develop affordable filtration systems using locally sourced materials. "
            "My goal is to empower communities through sustainable water management education."
        ),
        "goals": [
            "Pilot low-cost water filters in villages",
            "Train local technicians for maintenance",
            "Create educational campaigns on water hygiene"
        ],
        "email": "farid@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "gina",
        "description": (
            "I’m a documentary filmmaker focusing on social justice and human rights issues. "
            "My latest project examines the challenges faced by migrant workers globally. "
            "I aim to amplify marginalized voices through storytelling and community screenings."
        ),
        "goals": [
            "Complete a documentary on migrant labor",
            "Organize screening events with panel discussions",
            "Collaborate with advocacy organizations"
        ],
        "email": "gina@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "henry",
        "description": (
            "I’m an AI researcher passionate about ethical machine learning applications. "
            "I focus on fairness and transparency in algorithmic decision-making. "
            "My work involves developing tools to audit AI systems for bias."
        ),
        "goals": [
            "Develop open-source fairness evaluation tools",
            "Publish papers on AI ethics",
            "Host workshops for AI developers on bias mitigation"
        ],
        "email": "henry@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "isabel",
        "description": (
            "I’m a community organizer dedicated to improving housing rights in urban areas. "
            "I collaborate with tenants to fight eviction and advocate for affordable housing policies. "
            "My work emphasizes empowering residents through education and direct action."
        ),
        "goals": [
            "Create tenant legal support resources",
            "Organize community housing forums",
            "Lobby for rent control legislation"
        ],
        "email": "isabel@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "jacob",
        "description": (
            "I’m a musician blending traditional folk with electronic music to tell cultural stories. "
            "I teach workshops on songwriting and music production to youth in my community. "
            "My goal is to preserve heritage while innovating new soundscapes."
        ),
        "goals": [
            "Produce an album mixing folk and electronic styles",
            "Lead songwriting retreats",
            "Develop music education programs in schools"
        ],
        "email": "jacob@example.com",
        "password": generate_password_hash("password123")
    },
]
users += [
    {
        "name": "karen",
        "description": (
            "I’m a policy analyst specializing in education reform and equity. "
            "I work with school districts to design inclusive curricula that reflect diverse histories. "
            "My mission is to close achievement gaps and empower students from all backgrounds."
        ),
        "goals": [
            "Draft inclusive history lesson plans",
            "Host teacher training seminars",
            "Advocate for equitable funding policies"
        ],
        "email": "karen@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "leo",
        "description": (
            "As a mechanical engineer, I develop affordable assistive devices for people with disabilities. "
            "I focus on open-source designs that communities can build themselves. "
            "I’m passionate about combining technology and empathy to improve quality of life."
        ),
        "goals": [
            "Design modular prosthetic limbs",
            "Run community maker workshops",
            "Publish open hardware manuals"
        ],
        "email": "leo@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "maya",
        "description": (
            "I’m a mental health counselor working to destigmatize therapy in minority communities. "
            "I provide culturally sensitive support and facilitate group workshops. "
            "My goal is to increase access and awareness through outreach and education."
        ),
        "goals": [
            "Develop mental health outreach programs",
            "Partner with community centers for workshops",
            "Create multilingual resource materials"
        ],
        "email": "maya@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "nathan",
        "description": (
            "I’m a data analyst focused on urban mobility and sustainable transportation. "
            "I work with city planners to use data-driven insights to reduce congestion and emissions. "
            "I’m passionate about creating cities that prioritize people over cars."
        ),
        "goals": [
            "Build open data dashboards for traffic patterns",
            "Advocate for bike-friendly infrastructure",
            "Organize urban mobility hackathons"
        ],
        "email": "nathan@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "olga",
        "description": (
            "I’m a graphic designer who combines art and activism to raise awareness on social issues. "
            "I collaborate with nonprofits to create compelling visual campaigns. "
            "My work aims to inspire empathy and action through design."
        ),
        "goals": [
            "Design campaign materials for nonprofits",
            "Host community mural projects",
            "Teach design for social change workshops"
        ],
        "email": "olga@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "paul",
        "description": (
            "As a climate policy advocate, I work to influence legislation that reduces carbon emissions. "
            "I coordinate grassroots campaigns and engage stakeholders across sectors. "
            "I’m committed to accelerating the transition to renewable energy."
        ),
        "goals": [
            "Lobby for stricter emission standards",
            "Mobilize community climate actions",
            "Publish white papers on renewable policy"
        ],
        "email": "paul@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "quincy",
        "description": (
            "I’m a UX researcher studying how people interact with educational technology. "
            "My work focuses on making learning tools accessible to neurodiverse users. "
            "I collaborate with designers and educators to create inclusive experiences."
        ),
        "goals": [
            "Conduct usability studies on edtech platforms",
            "Develop accessibility guidelines",
            "Publish research on inclusive design"
        ],
        "email": "quincy@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "rachel",
        "description": (
            "I’m a social worker supporting homeless youth with housing and employment services. "
            "I build partnerships with local agencies to provide comprehensive care. "
            "I’m passionate about creating long-term stability and empowerment for vulnerable populations."
        ),
        "goals": [
            "Create job training programs for youth",
            "Expand emergency housing options",
            "Develop peer mentorship initiatives"
        ],
        "email": "rachel@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "samuel",
        "description": (
            "I’m a renewable energy engineer focused on solar panel efficiency improvements. "
            "I conduct research on new materials and design scalable solutions for developing regions. "
            "I believe renewable energy access is key to global equity."
        ),
        "goals": [
            "Prototype next-gen photovoltaic cells",
            "Collaborate with NGOs for solar installations",
            "Host educational workshops on renewables"
        ],
        "email": "samuel@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "tara",
        "description": (
            "I’m an educational technologist developing tools for remote learning in underserved schools. "
            "I focus on intuitive design that adapts to diverse learning styles. "
            "My aim is to reduce the digital divide through innovative solutions."
        ),
        "goals": [
            "Build adaptive learning software",
            "Partner with schools for pilot programs",
            "Train teachers in technology integration"
        ],
        "email": "tara@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "umar",
        "description": (
            "I’m a financial literacy coach helping low-income families build savings and credit. "
            "I develop workshops tailored to cultural contexts and economic challenges. "
            "My goal is to empower communities to achieve financial independence."
        ),
        "goals": [
            "Create budgeting and credit-building courses",
            "Partner with community banks for support",
            "Develop multilingual financial resources"
        ],
        "email": "umar@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "vanessa",
        "description": (
            "I’m a cultural anthropologist studying the impact of globalization on indigenous communities. "
            "I conduct fieldwork and collaborate on preservation of languages and traditions. "
            "I aim to promote cultural sustainability through education and advocacy."
        ),
        "goals": [
            "Document endangered languages",
            "Develop cultural exchange programs",
            "Publish accessible anthropology materials"
        ],
        "email": "vanessa@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "william",
        "description": (
            "I’m a chef and food justice advocate working to increase access to healthy meals. "
            "I run community kitchens and support urban agriculture initiatives. "
            "My passion is creating food systems that prioritize equity and sustainability."
        ),
        "goals": [
            "Launch a farm-to-table community cafe",
            "Organize cooking workshops on nutrition",
            "Advocate for local food policies"
        ],
        "email": "william@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "xenia",
        "description": (
            "I’m a marine biologist studying coral reef restoration and ocean health. "
            "I collaborate with international teams to develop sustainable conservation methods. "
            "I’m dedicated to educating communities on the importance of marine ecosystems."
        ),
        "goals": [
            "Lead coral nursery projects",
            "Create educational programs for schools",
            "Publish research on reef resilience"
        ],
        "email": "xenia@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "yusuf",
        "description": (
            "I’m a cybersecurity expert focused on protecting nonprofit organizations from cyber threats. "
            "I develop training programs and security audits tailored to resource-limited groups. "
            "My goal is to strengthen digital safety for social impact initiatives."
        ),
        "goals": [
            "Create cybersecurity awareness workshops",
            "Implement affordable security tools",
            "Partner with NGOs for risk assessments"
        ],
        "email": "yusuf@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "zoe",
        "description": (
            "I’m a poet and educator using literature to explore identity and social justice. "
            "I conduct writing workshops in underserved schools and community centers. "
            "My work seeks to empower voices through creative expression."
        ),
        "goals": [
            "Publish a poetry collection on social themes",
            "Host youth writing residencies",
            "Collaborate with activists on storytelling projects"
        ],
        "email": "zoe@example.com",
        "password": generate_password_hash("password123")
    },

    # 75 more to go, continuing in this style...

    {
        "name": "adrian",
        "description": (
            "I’m a startup founder creating AI tools for environmental monitoring. "
            "I work at the intersection of technology and sustainability to drive actionable insights. "
            "My passion is empowering communities to protect natural resources."
        ),
        "goals": [
            "Develop AI-powered sensor networks",
            "Partner with environmental NGOs",
            "Create open data platforms for climate action"
        ],
        "email": "adrian@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "bella",
        "description": (
            "I’m a public librarian promoting digital literacy and lifelong learning. "
            "I organize workshops on everything from coding to creative writing. "
            "My goal is to make knowledge accessible to all."
        ),
        "goals": [
            "Launch a digital literacy series",
            "Create community reading programs",
            "Develop accessible online resources"
        ],
        "email": "bella@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "carlos",
        "description": (
            "I’m an urban ecologist studying how green infrastructure benefits city health. "
            "I collaborate with local governments to implement sustainable landscaping. "
            "I’m passionate about bridging ecology and urban planning."
        ),
        "goals": [
            "Map urban biodiversity hotspots",
            "Advocate for green rooftops and parks",
            "Publish case studies on urban ecosystems"
        ],
        "email": "carlos@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "danielle",
        "description": (
            "I’m a social media strategist helping nonprofits amplify their missions. "
            "I design campaigns that engage audiences and drive support. "
            "My focus is on storytelling that inspires change."
        ),
        "goals": [
            "Create viral advocacy content",
            "Train nonprofit teams on digital marketing",
            "Measure impact through data analytics"
        ],
        "email": "danielle@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "elijah",
        "description": (
            "I’m a mechanical engineer designing energy-efficient appliances for developing markets. "
            "I work to reduce environmental impact while improving quality of life. "
            "My goal is to innovate practical solutions accessible to all."
        ),
        "goals": [
            "Develop low-power refrigeration units",
            "Pilot appliances in rural areas",
            "Collaborate with NGOs for distribution"
        ],
        "email": "elijah@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "fiona",
        "description": (
            "I’m a speech therapist specializing in bilingual populations. "
            "I develop tailored interventions to support language development. "
            "I’m passionate about equitable access to speech therapy services."
        ),
        "goals": [
            "Create bilingual therapy resources",
            "Train community health workers",
            "Conduct outreach in underserved areas"
        ],
        "email": "fiona@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "gabriel",
        "description": (
            "I’m a community health worker focusing on diabetes prevention and management. "
            "I provide education and support tailored to cultural needs. "
            "My goal is to reduce health disparities through prevention programs."
        ),
        "goals": [
            "Develop culturally relevant materials",
            "Host community health screenings",
            "Partner with clinics for follow-up care"
        ],
        "email": "gabriel@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "hannah",
        "description": (
            "I’m an environmental educator creating hands-on learning experiences for youth. "
            "I lead outdoor programs to foster stewardship and curiosity. "
            "I believe education is key to long-term environmental health."
        ),
        "goals": [
            "Organize nature camps",
            "Develop curriculum on sustainability",
            "Partner with schools for field trips"
        ],
        "email": "hannah@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "ian",
        "description": (
            "I’m a web developer building platforms that connect volunteers with causes. "
            "I focus on user-friendly interfaces and seamless experiences. "
            "My passion is empowering communities through technology."
        ),
        "goals": [
            "Launch a volunteer matching app",
            "Integrate event management features",
            "Collaborate with nonprofits on UX design"
        ],
        "email": "ian@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "julia",
        "description": (
            "I’m an economist studying the impacts of microfinance in emerging markets. "
            "I analyze data to understand how small loans affect community development. "
            "My goal is to improve financial inclusion globally."
        ),
        "goals": [
            "Publish studies on microloan outcomes",
            "Advise NGOs on financial program design",
            "Conduct workshops on economic empowerment"
        ],
        "email": "julia@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "kevin",
        "description": (
            "I’m a civil engineer working on sustainable water infrastructure projects. "
            "I aim to design systems that conserve resources and improve resilience. "
            "My passion is creating lasting solutions for water access."
        ),
        "goals": [
            "Design rainwater harvesting systems",
            "Implement water recycling projects",
            "Collaborate with communities for maintenance"
        ],
        "email": "kevin@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "lena",
        "description": (
            "I’m a filmmaker documenting environmental justice struggles worldwide. "
            "I focus on stories that highlight grassroots activism. "
            "My work seeks to inspire policy change through visual storytelling."
        ),
        "goals": [
            "Produce a documentary on water rights",
            "Organize film screenings and discussions",
            "Partner with advocacy groups"
        ],
        "email": "lena@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "michael",
        "description": (
            "I’m a robotics engineer creating assistive technologies for the elderly. "
            "I develop intuitive devices that support independence. "
            "My goal is to improve quality of life through innovation."
        ),
        "goals": [
            "Prototype robotic mobility aids",
            "Run user testing with seniors",
            "Collaborate with healthcare providers"
        ],
        "email": "michael@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "nina",
        "description": (
            "I’m a nutritionist promoting healthy eating habits in low-income communities. "
            "I design programs that respect cultural preferences and budget constraints. "
            "I believe in food as medicine and education as prevention."
        ),
        "goals": [
            "Create culturally tailored meal plans",
            "Conduct cooking demonstrations",
            "Partner with local markets for fresh produce"
        ],
        "email": "nina@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "owen",
        "description": (
            "I’m a teacher innovating curriculum for STEM education in under-resourced schools. "
            "I integrate project-based learning and real-world applications. "
            "My goal is to inspire curiosity and lifelong learning."
        ),
        "goals": [
            "Develop hands-on science kits",
            "Host STEM clubs and competitions",
            "Train teachers on active learning methods"
        ],
        "email": "owen@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "paula",
        "description": (
            "I’m a social entrepreneur creating affordable housing solutions using sustainable materials. "
            "I work with communities to co-design homes that meet local needs. "
            "My mission is to make safe, dignified housing accessible."
        ),
        "goals": [
            "Pilot sustainable housing projects",
            "Source eco-friendly building materials",
            "Train local builders in new techniques"
        ],
        "email": "paula@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "quentin",
        "description": (
            "I’m a linguist documenting endangered languages and developing revitalization programs. "
            "I collaborate with native speakers to preserve oral histories. "
            "My passion is keeping linguistic diversity alive."
        ),
        "goals": [
            "Record and archive rare languages",
            "Develop language learning apps",
            "Host community language workshops"
        ],
        "email": "quentin@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "rebecca",
        "description": (
            "I’m a psychologist researching trauma recovery and resilience in refugee populations. "
            "I design culturally informed therapeutic interventions. "
            "My goal is to support healing and empowerment."
        ),
        "goals": [
            "Conduct field research with displaced communities",
            "Develop trauma-informed counseling programs",
            "Train local mental health workers"
        ],
        "email": "rebecca@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "steven",
        "description": (
            "I’m a software engineer focused on blockchain applications for supply chain transparency. "
            "I develop tools that increase accountability in global trade. "
            "My work aims to reduce corruption and improve ethical sourcing."
        ),
        "goals": [
            "Build blockchain prototypes for supply chains",
            "Collaborate with ethical trade organizations",
            "Publish open-source toolkits"
        ],
        "email": "steven@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "tamara",
        "description": (
            "I’m a public health nurse leading vaccination campaigns in underserved areas. "
            "I focus on education and trust-building to improve immunization rates. "
            "My mission is to protect vulnerable populations from preventable diseases."
        ),
        "goals": [
            "Organize mobile vaccination clinics",
            "Create culturally sensitive educational materials",
            "Train community health volunteers"
        ],
        "email": "tamara@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "ursula",
        "description": (
            "I’m a conservation biologist working to protect endangered species habitats. "
            "I conduct field research and engage local communities in stewardship. "
            "I’m dedicated to preserving biodiversity through science and collaboration."
        ),
        "goals": [
            "Monitor wildlife populations",
            "Develop community conservation programs",
            "Publish scientific articles on habitat restoration"
        ],
        "email": "ursula@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "victor",
        "description": (
            "I’m an architect designing affordable, resilient buildings in disaster-prone regions. "
            "I emphasize sustainable materials and local construction methods. "
            "My goal is to create safe homes that withstand environmental challenges."
        ),
        "goals": [
            "Design prototype resilient housing",
            "Train builders in sustainable construction",
            "Collaborate with NGOs for disaster relief"
        ],
        "email": "victor@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "wanda",
        "description": (
            "I’m a community theater director using performing arts to explore social justice themes. "
            "I work with marginalized groups to tell their stories on stage. "
            "My passion is fostering empathy and dialogue through art."
        ),
        "goals": [
            "Produce plays on racial equity",
            "Conduct theater workshops for youth",
            "Partner with advocacy organizations"
        ],
        "email": "wanda@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "xander",
        "description": (
            "I’m a mechanical engineer specializing in sustainable transportation technologies. "
            "I develop efficient electric vehicle components and advocate for green mobility. "
            "My mission is to reduce transportation’s carbon footprint."
        ),
        "goals": [
            "Prototype electric drivetrain systems",
            "Collaborate on urban green mobility projects",
            "Publish research on transport sustainability"
        ],
        "email": "xander@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "yasmin",
        "description": (
            "I’m a social media content creator focused on mental health awareness. "
            "I share personal stories and practical advice to reduce stigma. "
            "My goal is to build a supportive online community."
        ),
        "goals": [
            "Create video series on coping strategies",
            "Host live Q&A sessions with professionals",
            "Collaborate with mental health organizations"
        ],
        "email": "yasmin@example.com",
        "password": generate_password_hash("password123")
    },
    {
        "name": "zachary",
        "description": (
            "I’m a software developer building educational games that teach coding to kids. "
            "I focus on making learning fun and accessible to diverse learners. "
            "My passion is empowering the next generation of tech innovators."
        ),
        "goals": [
            "Develop interactive coding games",
            "Partner with schools for pilot testing",
            "Create multilingual versions of games"
        ],
        "email": "zachary@example.com",
        "password": generate_password_hash("password123")
    }
]


accounts = [
    {
        "username": user["name"],
        "email": f"{user['name']}@example.com",
        "password": generate_password_hash("password123")
    }
    for user in users
]
