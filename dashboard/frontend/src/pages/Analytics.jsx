import Charts from "../components/Charts";

import "../assets/styles/analytics.css";

function Analytics() {

    const complianceTrend = {

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

                label: "Compliance Score",

                data: [

                    72,
                    75,
                    81,
                    87,
                    92,
                    96

                ],

                borderColor: "#2563EB",

                backgroundColor: "#93C5FD",

                tension: 0.4

            }

        ]

    };

    const scanTrend = {

        labels: [

            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4"

        ],

        datasets: [

            {

                label: "Weekly Scans",

                data: [

                    10,
                    15,
                    18,
                    24

                ],

                backgroundColor: "#2563EB"

            }

        ]

    };

    const licenseDistribution = {

        labels: [

            "MIT",
            "Apache-2.0",
            "GPL",
            "BSD",
            "Other"

        ],

        datasets: [

            {

                data: [

                    35,
                    28,
                    15,
                    12,
                    10

                ],

                backgroundColor: [

                    "#2563EB",
                    "#16A34A",
                    "#F59E0B",
                    "#DC2626",
                    "#8B5CF6"

                ]

            }

        ]

    };

    return (

        <div className="analytics-page">

            <h2>Analytics Dashboard</h2>

            <p>

                Executive insights across OSS audits, compliance and cryptographic analysis.

            </p>

            <div className="analytics-grid">

                <Charts

                    title="Compliance Trend"

                    type="line"

                    data={complianceTrend}

                />

                <Charts

                    title="Weekly Scan Trend"

                    type="bar"

                    data={scanTrend}

                />

                <Charts

                    title="License Distribution"

                    type="pie"

                    data={licenseDistribution}

                />

            </div>

        </div>

    );

}

export default Analytics;
