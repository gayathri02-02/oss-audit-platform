import FolderIcon from "@mui/icons-material/Folder";
import DescriptionIcon from "@mui/icons-material/Description";
import SecurityIcon from "@mui/icons-material/Security";
import AssessmentIcon from "@mui/icons-material/Assessment";

import ProjectCard from "../components/ProjectCard";
import Charts from "../components/Charts";

import "../assets/styles/dashboard.css";

function Home() {

    const complianceData = {

        labels: [

            "Jan",

            "Feb",

            "Mar",

            "Apr",

            "May",

            "Jun"

        ],

        datasets: [

            {

                label: "Compliance",

                data: [

                    72,

                    76,

                    81,

                    85,

                    91,

                    96

                ],

                borderColor: "#2563EB",

                backgroundColor: "#93C5FD",

                tension: 0.4

            }

        ]

    };

    const weeklyData = {

        labels: [

            "Week 1",

            "Week 2",

            "Week 3",

            "Week 4"

        ],

        datasets: [

            {

                label: "Projects Scanned",

                data: [

                    12,

                    18,

                    20,

                    25

                ],

                backgroundColor: "#2563EB"

            }

        ]

    };

    return (

        <div>

            <h2>Executive Dashboard</h2>

            <div className="dashboard-cards">

                <ProjectCard

                    title="Projects"

                    value="25"

                    color="#2563EB"

                    icon={<FolderIcon />}

                />

                <ProjectCard

                    title="SBOMs"

                    value="25"

                    color="#16A34A"

                    icon={<DescriptionIcon />}

                />

                <ProjectCard

                    title="CBOMs"

                    value="25"

                    color="#F59E0B"

                    icon={<SecurityIcon />}

                />

                <ProjectCard

                    title="Reports"

                    value="25"

                    color="#DC2626"

                    icon={<AssessmentIcon />}

                />

            </div>

            <div className="charts-grid">

                <Charts

                    title="Compliance Trend"

                    type="line"

                    data={complianceData}

                />

                <Charts

                    title="Weekly Scans"

                    type="bar"

                    data={weeklyData}

                />

            </div>

        </div>

    );

}

export default Home;
