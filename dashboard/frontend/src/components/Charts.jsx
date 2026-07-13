import {

    Chart as ChartJS,

    CategoryScale,

    LinearScale,

    PointElement,

    LineElement,

    BarElement,

    ArcElement,

    Title,

    Tooltip,

    Legend

} from "chart.js";

import {

    Line,

    Bar,

    Pie

} from "react-chartjs-2";

import "../assets/styles/charts.css";

ChartJS.register(

    CategoryScale,

    LinearScale,

    PointElement,

    LineElement,

    BarElement,

    ArcElement,

    Title,

    Tooltip,

    Legend

);

function Charts({

    title,

    type,

    data

}) {

    return (

        <div className="chart-card">

            <h3>{title}</h3>

            {

                type === "line" &&

                <Line data={data} />

            }

            {

                type === "bar" &&

                <Bar data={data} />

            }

            {

                type === "pie" &&

                <Pie data={data} />

            }

        </div>

    );

}

export default Charts;
