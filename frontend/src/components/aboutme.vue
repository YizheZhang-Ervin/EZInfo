<template>
	<section class="whole">
		<!-- 左侧菜单 -->
		<el-menu
			class="menu"
			:collapse="navCollapse"
			background-color="#142044"
			text-color="darkgrey"
			active-text-color="beige"
		>
			<el-image :src="self.nav" fit="cover" class="nav-img"></el-image>
			<el-divider content-position="center">Ervin</el-divider>
			<el-menu-item route="name">
				<a href="#summary" class="menulink">
					<i class="el-icon-star-off"></i>
					<span slot="title">Yizhe Zhang</span></a
				>
			</el-menu-item>
			<el-menu-item index="school">
				<a href="#education" class="menulink">
					<i class="el-icon-school"></i>
					<span slot="title">NEU</span>
				</a>
			</el-menu-item>
			<el-menu-item index="pre">
				<a href="#certificate" class="menulink">
					<i class="el-icon-s-platform"></i>
					<span slot="title">Information Systems</span></a
				>
			</el-menu-item>
			<el-submenu index="contact">
				<template slot="title">
					<i class="el-icon-phone-outline"></i>
					<span>Contact</span>
				</template>

				<a
					target="_blank"
					rel="noopener noreferrer"
					href="mailto:zhang.yizhe@northeastern.edu?subject=Please%20type%20in%20the%20subject"
					><el-menu-item index="email">Email</el-menu-item></a
				>
				<a
					target="_blank"
					rel="noopener noreferrer"
					href="https://www.linkedin.com/in/yizhe-zhang"
					><el-menu-item index="linkedin">Linkedin</el-menu-item></a
				>
				<a
					target="_blank"
					rel="noopener noreferrer"
					href="https://github.com/YizheZhang-Ervin"
					><el-menu-item index="github">Github</el-menu-item></a
				>
				<a
					target="_blank"
					rel="noopener noreferrer"
					href="https://www.zhihu.com/people/yizhezhang"
					><el-menu-item index="zhihu">Zhihu</el-menu-item></a
				>
				<a href="/static/ezapp.apk" download="ezapp.apk"
					><el-menu-item index="apk">Personal App</el-menu-item></a
				>
			</el-submenu>
			<el-menu-item index="hide" @click="changeCollapse">
				<i class="el-icon-s-fold"></i>
				<span>Hide</span>
			</el-menu-item>
		</el-menu>
		<!-- 右侧 -->
		<div class="rightArea">
			<!-- carousel -->
			<el-carousel class="carousel" type="card">
				<el-carousel-item
					v-for="item in carousel"
					:key="item"
					style="display: flex; justify-content: center"
				>
					<img :src="item" style="height: 300px" />
				</el-carousel-item>
			</el-carousel>
			<!-- Summary -->
			<a name="summary"></a>
			<el-divider></el-divider>
			<el-divider content-position="left">
				<i class="el-icon-star-on"></i> Summary
			</el-divider>
			<section class="summary">
				<!-- <el-image :src="self.summary" fit="contain" class="summary-img" ></el-image> -->
				<div class="card-outer">
					<el-card
						shadow="hover"
						v-for="s in summary"
						:key="s.title"
						class="cards"
					>
						<div slot="header">
							{{ s.title }}
						</div>
						<div>
							{{ s.detail }}
						</div>
						<br/>Top3:  
						<el-tag :type="tag.type" v-for="tag in s.tags" :key="tag.label">{{tag.label}}</el-tag>
					</el-card>
				</div>
			</section>
			<!-- Technology -->
			<a name="technology"></a>
			<el-divider></el-divider>
			<el-divider content-position="left">
				<i class="el-icon-s-platform"></i> Technology</el-divider
			>
			<section>
				<el-collapse v-model="collapseTechnology" accordion>
					<el-collapse-item
						:title="tech.title"
						:name="tech.title"
						v-for="tech in technology"
						:key="tech.title"
					>
						<div v-for="tt in tech.content" :key="tt">
							<p class="techs">{{ tt }}</p>
						</div>
					</el-collapse-item>
				</el-collapse>
			</section>
			<!-- Certificates -->
			<a name="certificate"></a>
			<el-divider></el-divider>
			<el-divider content-position="left">
				<i class="el-icon-medal"></i> Certificates</el-divider
			>
			<section>
				<el-collapse v-model="collapseCertificate" accordion>
					<el-collapse-item
						:title="cer.title"
						:name="cer.title"
						v-for="cer in certificates"
						:key="cer.title"
					>
						<div>
							<p>{{ cer.time }}</p>
							<a target="_blank" :href="cer.href">Certificate Link</a>
							<br /><br />
							<el-image :src="cer.img"></el-image>
						</div>
					</el-collapse-item>
				</el-collapse>
			</section>
			<!-- Education -->
			<a name="education"></a>
			<el-divider></el-divider>
			<el-divider content-position="left">
				<i class="el-icon-school"></i> Education</el-divider
			>
			<section>
				<el-card
					shadow="hover"
					v-for="ed in education"
					:key="ed.title"
					class="cards"
				>
					<div slot="header" class="flex-card-title">
						<p>{{ ed.title }}</p>
						<a target="_blank" :href="ed.href">School Link</a>
					</div>
					<div>
						<p>{{ ed.degree }}</p>
						<p>{{ ed.time }}</p>
						<br />
						<el-image :src="ed.img"></el-image>
					</div>
				</el-card>
			</section>
			<!-- Projects -->
			<a name="project"></a>
			<el-divider></el-divider>
			<el-divider content-position="left">
				<i class="el-icon-notebook-1"></i> Projects</el-divider
			>
			<section>
				<el-collapse v-model="collapseProject">
					<!-- 2021 -->
					<el-divider>2021</el-divider>
					<el-collapse-item
						:title="prj.title"
						:name="prj.title"
						v-for="prj in project2021"
						:key="prj.title"
					>
						<div class="flex-card-title">
							<p>{{ prj.tech }}</p>
							<p>{{ prj.time }}</p>
							<a target="_blank" :href="prj.href">Github Link</a>
						</div>
					</el-collapse-item>
					<!-- 2020 -->
					<el-divider>2020</el-divider>
					<el-collapse-item
						:title="prj.title"
						:name="prj.title"
						v-for="prj in project2020"
						:key="prj.title"
					>
						<div class="flex-card-title">
							<p>{{ prj.tech }}</p>
							<p>{{ prj.time }}</p>
							<a target="_blank" :href="prj.href">Github Link</a>
						</div>
					</el-collapse-item>
					<!-- 2019 -->
					<el-divider>2019</el-divider>
					<el-collapse-item
						:title="prj.title"
						:name="prj.title"
						v-for="prj in project2019"
						:key="prj.title"
					>
						<div class="flex-card-title">
							<p>{{ prj.tech }}</p>
							<p>{{ prj.time }}</p>
							<a target="_blank" :href="prj.href">Github Link</a>
						</div>
					</el-collapse-item>
				</el-collapse>
			</section>
		</div>
	</section>
</template>

<script>
export default {
	name: "Aboutme",
	data() {
		return {
			summary: [
				{
					title: "Hard Power",
					detail: `A full stack engineer who is proficient in Front-End and Back-End development of Websites.
                    Be familiar with mainstream frameworks such as React/Angular/Vue/RN(Front-End), Django/Express(Back-End).
                    Developed several individual&team projects.
                    Good at optimizing user experience and improving project quality through data analysis.`,
					tags:[{type:"",label:"Meteor Home Rent"},
					{type:"success",label:"Sharing Bike System"},
					{type:"info",label:"EZ Info Blog"}]
				},
				{
					title: "Soft Power",
					detail: `Conscientious, responsible and well-organized.
                        Have Strong adaptability and can quickly integrate into the team.
                        Have strong learning ability and can quickly master the knowledge structure.
                        Love to track the latest Front-End technology.
                        Rigorous, neat and high-quality code style.`,
					tags:[{type:"info",label:"Modest"},
					{type:"",label:"Gentle"},
					{type:"success",label:"Cautious"}]
				},
			],
			self: {
				summary: require("../assets/static/img/myself/self_summary.png"),
				nav: require("../assets/static/img/myself/ervin2.jpg"),
			},
			technology: [
				{
					title: "Development",
					content: [
						"Progamming Language: Python, SQL, C++, C#, Java, Scala, GO",
						"FrontEnd Language: HTML / CSS / SASS, JavaScript / TypeScript",
						"FrontEnd Framework: Angular, React, Vue, Bootstrap, Antd, ElementUI, Ng-zorro",
						"BackEnd Framework: Django, Tornado, Flask, Express(Node.js), Meteor(Node.js)",
						"Database: Sqlite, MS SqlServer, Mysql, Oracle, PostgreSql, MongoDB",
						"DevOps: Webpack, Nginx, Docker, K8S, AWS, Git, Postman",
						"Testing: Selenium",
						"GUI/Game: Unity3d, Unreal, Tkinter, Pyqt, Pygame",
						"OS: Windows, Linux",
					],
				},
				{
					title: "Data",
					content: [
						"Data Crawler: Requests+BeautifulSoup, Scrapy+Selenium",
						"Data Process: Numpy, Pandas, Scipy, Sklearn, Matplotlib, Seaborn, Echarts",
						"Business Intelligence: Power BI, Tableau, SPSS, SSIS/SSAS/SSRS",
						"Big Data: Hadoop, Spark, Kafka",
						"Machine Learning / Artificial Intelligence: Tensorflow, Keras",
						"Finance Data: Mplfinance, Investpy, Trendet, Pynance",
					],
				},
				{
					title: "Other",
					content: [
						"MultiMedia: Corel VideoStudio, PhotoShop, Adobe Flash, Adobe Audition",
						"PM: Office, Figma, Axure RP, Adobe XD, Mind Manager",
					],
				},
			],
			certificates: [
				{
					title: "Data Analytics Consulting Virtual Internship",
					time: "KPMG (Issued Aug, 2020)",
					img: require("../assets/static/img/certificates/KPMG-DA.png"),
					href:
						"https://insidesherpa.s3.amazonaws.com/completion-certificates/KPMG/m7W4GMqeT3bh9Nb2c_KPMG_EaQWiwTz5acSuNWjd_completion_certificate.pdf",
				},
				{
					title: "Software Engineering Virtual Experience",
					time: "JPMorgan Chase & Co (Issued Aug, 2020)",
					img: require("../assets/static/img/certificates/jpmorgan-se.png"),
					href:
						"https://insidesherpa.s3.amazonaws.com/completion-certificates/JP%20Morgan/R5iK7HMxJGBgaSbvk_JPMorgan%20Chase_EaQWiwTz5acSuNWjd_completion_certificate.pdf",
				},
				{
					title: "Google Analytics Individual Qualification",
					time: "Google (Issued Aug, 2020)",
					img: require("../assets/static/img/certificates/GAIQ.png"),
					href: "https://skillshop.exceedlms.com/student/award/56443312",
				},
				{
					title: "Data Analytics Program",
					time: "General Electric (Issued Aug, 2020)",
					img: require("../assets/static/img/certificates/GE-DA.png"),
					href:
						"https://insidesherpa.s3.amazonaws.com/completion-certificates/General%20Electric%20%28GE%29/ThbphD5N5WRsd9Mxo_General%20Electric_EaQWiwTz5acSuNWjd_completion_certificate.pdf",
				},
				{
					title: "Go.Data",
					time: "World Health Organization (Issued Aug, 2020)",
					img: require("../assets/static/img/certificates/WHO-godata.png"),
					href: "https://www.who.int/",
				},
				{
					title: "Visualization Data By Python",
					time: "IBM (Issued May, 2020)",
					img: require("../assets/static/img/certificates/IBM_python.jpg"),
					href:
						"https://courses.edx.org/certificates/1ce4ab37a776413595b03e884461c396",
				},
				{
					title: "Python 3",
					time: "SoloLearn (Issued December, 2019)",
					img: require("../assets/static/img/certificates/python3.jpg"),
					href: "http://www.linkedin.com/in/yizhe-zhang",
				},
				{
					title: "JavaScript",
					time: "SoloLearn (Issued December, 2019)",
					img: require("../assets/static/img/certificates/js.jpg"),
					href: "http://www.linkedin.com/in/yizhe-zhang",
				},
				{
					title: "BI Developer",
					time: "Bluelime (Issued November,2019)",
					img: require("../assets/static/img/certificates/bi.jpg"),
					href: "https://www.udemy.com/certificate/UC-D2TDUN3J/",
				},
			],
			education: [
				{
					title: "Northeastern University, Boston, MA, United States",
					time: "2019 - Present",
					degree: "Master of Science in Information Systems",
					href: "https://www.northeastern.edu/",
					img: require("../assets/static/img/school/neu.jpg"),
				},
				{
					title: "University of California, Los Angeles, CA, United States",
					time: "2017",
					degree:
						"Certificate of International Business & Leadership Management",
					href: "https://www.ucla.edu/",
					img: require("../assets/static/img/school/ucla.jpg"),
				},
				{
					title: "Nantong University, Nantong, Jiangsu, China",
					time: "2015 - 2019",
					degree:
						"Bachelor of Management in Information Management and Information System",
					href: "https://www.ntu.edu.cn/main.htm",
					img: require("../assets/static/img/school/ntu.jpg"),
				},
			],
			project2021: [
				{
					title: "EZ Intelligence",
					time: "Feb 2021 - March 2021",
					tech: "React, Flask RESTful, Sqlite, Antd, Echarts",
					href: "https://github.com/YizheZhang-Ervin/EZIntelligence",
				},
				{
					title: "EZ Info",
					time: "Jan 2021 - Future",
					tech: "Vue, Django, Echarts, ElementUI, peerjs",
					href: "https://github.com/YizheZhang-Ervin/EZInfo",
				},
				{
					title: "EGGroup WebGL",
					time: "Jan 2021 - April 2021",
					tech: "Vue, Express, Mysql, ElementUI",
					href: "https://github.com/YizheZhang-Ervin/EGGroup_WebGL",
				},
				{
					title: "Sharing Bike System",
					time: "Jan 2021 - Feb 2021",
					tech: "React, Django, Antd, Sqlite, Echarts",
					href: "https://github.com/YizheZhang-Ervin/SharingBike",
				},
			],
			project2020: [
				{
					title: "Personal Website V3.0",
					time: "Oct 2020 - Feb 2021",
					tech: "Angular, Django, Sqlite",
					href: "https://github.com/YizheZhang-Ervin/EasyEZ_V3",
				},
				{
					title: "FinTech - Fixed Income Security (NS Model)",
					time: "Sept 2020 - Nov 2020",
					tech: "Vue, Flask, Echarts",
					href: "https://github.com/YizheZhang-Ervin/FinTech_FishGroup",
				},
				{
					title: "LinkedIn Network New Feature",
					time: "Sept 2020 - Nov 2020",
					tech: "Sketch, Wireframe, Prototype",
					href: "https://github.com/YizheZhang-Ervin/",
				},
				{
					title: "Screen Time App",
					time: "Sept 2020 - Nov 2020",
					tech: "Sketch, Wireframe, Prototype",
					href: "https://github.com/YizheZhang-Ervin/",
				},
				{
					title: "Quantitative Nutriology",
					time: "May 2020 - Sept 2020",
					tech: "Python",
					href:
						"https://github.com/YizheZhang-Ervin/Knowledge_QuantitativeNutriology",
				},
				{
					title: "Cryptography",
					time: "May 2020 - Sept 2020",
					tech: "Python",
					href: "https://github.com/YizheZhang-Ervin/Knowledge_Cryptography",
				},
				{
					title: "Cloud Storage App",
					time: "Apr 2020 - May 2020",
					tech: "Django, Bootstrap, Sqlite",
					href: "https://github.com/YizheZhang-Ervin/IMISCloud",
				},
				{
					title: "Personal Website V2.0",
					time: "Apr 2020 - May 2020",
					tech: "Bootstrap, Django, Mysql",
					href: "https://github.com/YizheZhang-Ervin/EasyEZ_V2",
				},
				{
					title: "FinTech - Gold Visualization",
					time: "Mar 2020 - Apr 2020",
					tech: "Tornado, Bootstrap, Sqlite",
					href: "https://github.com/YizheZhang-Ervin/FinTech_BEA",
				},
				{
					title: "Personal Website V1.0",
					time: "Jan 2020 - Apr 2020",
					tech: "Django, Mysql",
					href: "https://github.com/YizheZhang-Ervin/EasyEZ_V1",
				},
				{
					title: "Meteor Home - Home Rent Website",
					time: "Jan 2020 - Apr 2020",
					tech: "Angular, Express, MongoDB, Ng-Zorro",
					href: "https://github.com/YizheZhang-Ervin/MeteorHome",
				},
				{
					title: "To do List",
					time: "Jan 2020 - Apr 2020",
					tech: "Angular, Express, MongoDB",
					href:
						"https://github.com/YizheZhang-Ervin/Course_WebDesign/tree/master/Todolist",
				},
				{
					title: "MA Education Data Analysis",
					time: "Jan 2020 - Apr 2020",
					tech:
						"Python (Jupyter Notebook, Numpy, Pandas, Scipy, Sklearn, Matplotlib)",
					href: "",
				},
			],
			project2019: [
				{
					title: "Hotel Database System",
					time: "Sept 2019 - Dec 2019",
					tech: "Java, Sqlserver, Power BI",
					href: "https://github.com/YizheZhang-Ervin/Course_InfoSystems",
				},
				{
					title: "Hospital Information System",
					time: "Sept 2019 - Dec 2019",
					tech: "Java",
					href: "https://github.com/YizheZhang-Ervin/Course_InfoSystems",
				},
				{
					title: "Gamification Used by Exploratory Search System (GUESS)",
					time: "Sept 2018 - Jun 2019",
					tech: "Axure RP",
					href:
						"https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2020&filename=XDQB202004004&v=QvJXxfJ04mUgJFeK46HZB3jGJp5eqMM7Qdsj4Tv20LhbWiFXkr1pIAgL1aukIgd4",
				},
				{
					title: "Imitate Douban Website",
					time: "Sept 2018 - Jan 2019",
					tech: "JSP",
					href: "https://github.com/YizheZhang-Ervin/Course_JavaJSP",
				},
				{
					title: "Little Iron Pot App",
					time: "Mar 2018 - Jun 2018",
					tech: "MIT App Inventor",
					href: "",
				},
				{
					title: "Tank Battle Game",
					time: "Mar 2018 - Jun 2018",
					tech: "Java AWT",
					href: "https://github.com/YizheZhang-Ervin/Course_JavaJSP",
				},
			],
			carousel: [
				require("../assets/static/img/projects/1.png"),
				require("../assets/static/img/projects/2.png"),
				require("../assets/static/img/projects/3.png"),
				require("../assets/static/img/projects/4.png"),
			],
			navCollapse: true,
			collapseCertificate: "Data Analytics Consulting Virtual Internship",
			collapseProject: [
				"EZ Info",
				"Personal Website V3.0",
				"Hotel Database System",
			],
			collapseTechnology: "Development",
		};
	},
	mounted() {},
	methods: {
		changeCollapse() {
			this.navCollapse = !this.navCollapse;
		},
	},
};
</script>

<style scoped>
.el-divider__text {
	background-color: beige;
}

.menu .el-divider__text {
	background-color: rgb(20, 32, 68);
	color: beige;
	padding: 0 2%;
}

/* 整体 */
.whole {
	height: 100vh;
	width: 100vw;
	overflow: hidden;
	background: beige;
	display: flex;
	align-items: center;
	justify-content: space-between;
}

/* 左侧 */
.menu {
	height: 100vh;
	font-size: 0.8em;
	max-width: 200px;
	overflow-y: auto;
	overflow-x: hidden;
}

.nav-img {
	max-width: 100%;
}

/* 右侧 */
.rightArea {
	max-width: 100vw;
	width: 95vw;
	overflow-y: scroll;
	height: 100vh;
}
.summary-img {
	width: 20vw;
}

.cards {
	background-color: beige;
}

/* .card-outer {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 50vw;
} */

.summary {
	display: flex;
	align-items: center;
	justify-content: space-around;
}

a {
	text-decoration: none;
	color: darkgray;
}

.techs {
	line-height: 30px;
}

.flex-card-title {
	display: flex;
	align-items: center;
	justify-content: space-between;
}

.carousel-pic {
	height: 300px;
	width: 300px;
}

.menulink {
	display: inline-block;
	width: 100%;
}
</style>
