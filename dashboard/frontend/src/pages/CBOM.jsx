import { useState } from "react";

import DownloadIcon from "@mui/icons-material/Download";
import VisibilityIcon from "@mui/icons-material/Visibility";
import SearchIcon from "@mui/icons-material/Search";

import "../assets/styles/cbom.css";

function CBOM() {

    const [search, setSearch] = useState("");

    const [cboms] = useState([

        {
            id: 1,
            project: "ESP-IDF",
            file: "esp-idf_cbom.json",
            algorithms: 42,
            critical: 2,
            generated: "2026-07-10"
        },

        {
            id: 2,
            project: "Apache Fineract",
            file: "fineract_cbom.json",
            algorithms: 31,
            critical: 0,
            generated: "2026-07-11"
        },

        {
            id: 3,
            project: "Zephyr RTOS",
            file: "zephyr_cbom.json",
            algorithms: 27,
            critical: 1,
            generated: "2026-07-12"
        }

    ]);

    const filtered = cboms.filter(item =>
        item.project.toLowerCase().includes(search.toLowerCase()) ||
        item.file.toLowerCase().includes(search.toLowerCase())
    );

    return (

        <div className="cbom-page">

            <div className="page-header">

                <h2>Cryptography Bill of Materials (CBOM)</h2>

                <p>

                    Browse generated CBOMs and cryptographic inventory.

                </p>

            </div>

            <div className="search-container">

                <SearchIcon />

                <input
                    type="text"
                    placeholder="Search CBOM..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                />

            </div>

            <table className="cbom-table">

                <thead>

                    <tr>

                        <th>Project</th>

                        <th>CBOM File</th>

                        <th>Algorithms</th>

                        <th>Critical</th>

                        <th>Generated</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        filtered.map(cbom => (

                            <tr key={cbom.id}>

                                <td>{cbom.project}</td>

                                <td>{cbom.file}</td>

                                <td>{cbom.algorithms}</td>

                                <td>

                                    <span className={
                                        cbom.critical > 0
                                            ? "critical"
                                            : "safe"
                                    }>

                                        {cbom.critical}

                                    </span>

                                </td>

                                <td>{cbom.generated}</td>

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

export default CBOM;
