from pathlib import Path 
import streamlit as st
from PIL import Image	


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "ProfessionalSummary.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rishab Baid"
PAGE_ICON = ":wave:"
NAME = "Rishab Baid"
DESCRIPTION = """
|| Bigdata Developer at EPAM ||
"""
EMAIL = "rishab0202baid@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rishabkumarbaid/",
    "Instagram": "https://www.instagram.com/_baid_rishab_/"
}


PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(
	page_title=PAGE_TITLE,
	page_icon=PAGE_ICON
)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- 🔸 Working as Module Lead with almost 8+ years of total experience in IT industry.
- 🔸 4+ years of relevant experience in Hadoop and Big data technologies in Hospitality & Healthcare domain.
- 🔸 4+ years of experience in Mainframe technologies in Hospitality, Banking and Healthcare sector.
- 🔸 Proficient in using RDBMS like PostgreSQL and SQL Server and Cloud Storage like Snowflake
- 🔸 Good Exposure to AWS services.
- 🔸 Good experience in Spark architecture for processing large amount of data.
- 🔸 Have worked on Hive, Spark Core, RDD,SparkSQL with DataFrames & DataSets.
- 🔸 Have good experience in BI tools like Tableau and Power BI.
- 🔸 Strong communications, collaborations and interpersonal skills with proficiency on grasping new concepts quickly and utilizing them in an effective manner.
"""
)

# --- CERTIFICATION ---
st.write('\n')
st.subheader("Certification")
st.write(
    """
- 🗄️ Snowpro Core Certification issued by Snowflake – Jan 2023
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Scala, Python, Apache Spark, SQL
- 📊 Data Visulization: PowerBi, Tableau, Streamlit
- 📚 Modeling: 
- 🗄️ Databases: Snowflake
- 📃 AWS : S3, Glue, lambda, EMR, EC2, Athena, DMS, Airflow
"""
)

col = st.columns(5)


# --- JOB 5 ----
st.write("---")
st.subheader("📗 EPAM Systems")
st.write("2021-Nov-21 till present")
st.write("""
- 🔸 Currently working as a SSE in a project where we have built a Data quality framework on streaming platform involving various systems to validate data metrics such as completeness, coverage and consistency
- 🔸 Worked on developing Spark application as a complete package which consists of multiple readers and writers supporting different file formats.
- 🔸 Used AWS services like Lambda, Ec2, Glue and user written python code to retrieve data from various sources to dump in the unified Data lake storage.
- 🔸 Worked on automating recovery process to re-ingest lost data between the layers to ensure there are no data loss because of connectivity / unavailability.
- 🔸 Worked on creating multiple dashboards in Tableau and Power BI which helped in finding the errors in complete pipeline from end to end.
	""")


# --- JOB 4 ----
st.write("---")
st.subheader("📗 Legato Health Technologies")
st.write("2021-Jan-10 till 2021-Nov-21")
st.write("""
- 🔸 Worked as a technical lead in a project where we are migrating data from oracle to hdfs using bigdata technologies.
- 🔸 Part of development team, where we created a framework which can take any sql as input along with other parameters and load processed data into Hive.
- 🔸 Actively worked in the complete project architecture from end to end.
- 🔸 Creating designs for job to be implemented in Spark that includes HLD, LLD and development and then completing the end to end work of the module.
- 🔸 Taking responsibilities in development activities implementing solutions, including developer setup, build and release, packaging and configuring the environment.
	""")



# --- JOB 3 ----
st.write("---")
st.subheader("📗 Mindtree Pvt Ltd ")
st.write("2017-Aug-21 till 2021-Jan-08")
st.write("""
- 🔸 Currently working on a project which is migrating old legacy Mainframe system to Big data platform. There are multiple screens of Revenue management System, whose source must be converted as part of this project. Started this project by analyzing the complete system which was running on Mainframes.
- 🔸 Was actively involved with clients in gathering business requirements.
- 🔸 Creating designs for job to be implemented in Spark that includes HLD, LLD and development
- 🔸 Created the complete end to end data workflow for multiple modules. Actively involved as SME for giving KT to spark team members while designing the HLD and LLD.
- 🔸 Once the design was approved, have written the complete spark code using Spark, Scala.
	""")



# --- JOB 2 ----
st.write("---")
st.subheader("📗 Cerner Health Care Solutions Pvt Ltd")
st.write("2016-Aug-05 till 2017-Jun-09")
st.write("""
- 🔸 Project mainly deals in rectifying errors or making change as per the requirement in the Invision Product built on mainframes.
- 🔸 Analyzing, Coding, Unit Testing and Code Review.
- 🔸 Business process understanding and knowledge gathering.
- 🔸 Understanding the problem in the Invision System, this is customized differently for all the hospitals.
	""")



# --- JOB 1 ----
st.write("---")
st.subheader("📗 Cognizant Technology Solutions")
st.write("2014-Jul-04 till 2016-Aug-05")
st.write("""
- 🔸 Project mainly deals with the reformatting of unstructured data into structured data, creating appropriate flags after considering the business logics, so that it can be further moved into the database under Agile methodology.
- 🔸 Coding, Unit Testing, Code Review and Documentation.
- 🔸 Perform analysis on the application program(s) and prepare specification documents based on the program logic as per the requirement.
- 🔸 Resolving production queries/issues with efficient manner meeting SLA’s.
- 🔸 Co-ordination with onsite team members for various client specific task and requirement.
	""")















