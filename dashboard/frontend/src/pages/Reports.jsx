import { useState } from "react";

import DownloadIcon from "@mui/icons-material/Download";
import VisibilityIcon from "@mui/icons-material/Visibility";
import PictureAsPdfIcon from "@mui/icons-material/PictureAsPdf";
import SearchIcon from "@mui/icons-material/Search";

import "../assets/styles/reports.css";

function Reports() {

    const [search, setSearch] = useState("");

    const [reports] = useState([

        {

            id: 1,

            project: "ESP-IDF",

            report: "esp-idf_ai_report.pdf",

            score: "96%",

            generated: "2026-07-10",

            status: "Completed"

        },

        {

            id: 2,

            project: "Apache Fineract",

            report: "fineract_ai_report.pdf",

            score: "91%",

            generated: "2026-07-11",

            status: "Completed"

        },

        {

            id: 3,

            project: "Zephyr RTOS",

            report: "zephyr_ai_report.pdf",

            score: "88%",

            generated: "2026-07-12",

            status: "Completed"

        }

    ]);

    const filtered = reports.filter(item =>

        item.project.toLowerCase().includes(search.toLowerCase()) ||

        item.report.toLowerCase().includes(search.toLowerCase())

    );

    return (

        <div className="reports-page">

            <div className="page-header">

                <h2>AI Generated Reports</h2>

                <p>

                    Executive reports generated from SBOM and CBOM analysis.

                </p>

            </div>

            <div className="search-container">

                <SearchIcon />

                <input

                    type="text"

                    placeholder="Search Reports..."

                    value={search}

                    onChange={(e)=>setSearch(e.target.value)}

                />

            </div>

            <table className="reports-table">

                <thead>

                    <tr>

                        <th>Project</th>

                        <th>Report</th>

                        <th>Compliance</th>

                        <th>Generated</th>

                        <th>Status</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        filtered.map(report=>(

                            <tr key={report.id}>

                                <td>{report.project}</td>

                                <td>{report.report}</td>

                                <td>{report.score}</td>

                                <td>{report.generated}</td>

                                <td>

                                    <span className="completed">

                                        {report.status}

                                    </span>

                                </td>

                                <td>

                                    <button className="action-btn">

                                        <VisibilityIcon/>

                                    </button>

                                    <button className="action-btn">

                                        <PictureAsPdfIcon/>

                                    </button>

                                    <button className="action-btn">

                                        <DownloadIcon/>

                                    </button>

                                </td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </div>

    );

}

export default Reports;
