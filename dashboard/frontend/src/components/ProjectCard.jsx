import "../assets/styles/cards.css";

function ProjectCard({

    title,

    value,

    color,

    icon

}) {

    return (

        <div
            className="project-card"
            style={{

                borderLeft: `6px solid ${color}`

            }}
        >

            <div className="card-top">

                <div className="card-icon">

                    {icon}

                </div>

            </div>

            <div className="card-body">

                <h4>

                    {title}

                </h4>

                <h2>

                    {value}

                </h2>

            </div>

        </div>

    );

}

export default ProjectCard;
