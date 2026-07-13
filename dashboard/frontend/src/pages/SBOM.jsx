import { useState } from "react";

import DownloadIcon from "@mui/icons-material/Download";
import VisibilityIcon from "@mui/icons-material/Visibility";
import SearchIcon from "@mui/icons-material/Search";

import "../assets/styles/sbom.css";

function SBOM() {

    const [search, setSearch] = useState("");

    const [sboms] = useState([

        {
            id: 1,
            project: "ESP-IDF",
            file: "esp-idf_sbom.json",
            format: "CycloneDX",
            components: 1248,
            generated: "2026-07-10"
        },

        {
            id: 2,
            project: "Apache Fineract",
            file: "fineract_sbom.json",
            format: "CycloneDX",
            components: 2875,
            generated: "2026-07-11"
        },

        {
            id: 3,
            project: "Zephyr RTOS",
            file: "zephyr_sbom.json",
            format: "CycloneDX",
            components: 1836,
            generated: "2026-07-12"
        }

    ]);

    const filtered = sboms.filter(item =>
        item.project.toLowerCase().includes(search.toLowerCase()) ||
        item.file.toLowerCase().includes(search.toLowerCase())
    );

    return (

        <div className="sbom-page">

            <div className="page-header">

                <h2>Software Bill of Materials (SBOM)</h2>

                <p>
                    Browse generated SBOMs for all scanned repositories.
                </p>

            </div>

            <div className="search-container">

                <SearchIcon />

                <input
                    type="text"
                    placeholder="Search SBOM..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                />

            </div>

            <table className="sbom-table">

                <thead>

                    <tr>

                        <th>Project</th>

                        <th>SBOM File</th>

                        <th>Format</th>

                        <th>Components</th>

                        <th>Generated</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        filtered.map(sbom => (

                            <tr key={sbom.id}>

                                <td>{sbom.project}</td>

                                <td>{sbom.file}</td>

                                <td>{sbom.format}</td>

                                <td>{sbom.components}</td>

                                <td>{sbom.generated}</td>

                                <td>

                                    <button className="action-btn">

                                        <VisibilityIcon />

                                    </button>

                                    <button className="action-btn">

                                        <DownloadIcon />

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

export default SBOM;
