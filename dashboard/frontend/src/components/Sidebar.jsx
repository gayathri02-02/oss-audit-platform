import { Link, useLocation } from "react-router-dom";

import DashboardIcon from "@mui/icons-material/Dashboard";
import FolderIcon from "@mui/icons-material/Folder";
import DescriptionIcon from "@mui/icons-material/Description";
import SecurityIcon from "@mui/icons-material/Security";
import AssessmentIcon from "@mui/icons-material/Assessment";
import AnalyticsIcon from "@mui/icons-material/Analytics";

import "../assets/styles/sidebar.css";

const menuItems = [

    {
        name: "Dashboard",
        path: "/",
        icon: <DashboardIcon />
    },

    {
        name: "Projects",
        path: "/projects",
        icon: <FolderIcon />
    },

    {
        name: "SBOMs",
        path: "/sboms",
        icon: <DescriptionIcon />
    },

    {
        name: "CBOMs",
        path: "/cboms",
        icon: <SecurityIcon />
    },

    {
        name: "Reports",
        path: "/reports",
        icon: <AssessmentIcon />
    },

    {
        name: "Analytics",
        path: "/analytics",
        icon: <AnalyticsIcon />
    }

];

function Sidebar() {

    const location = useLocation();

    return (

        <div className="sidebar">

            <div className="sidebar-logo">

                <h2>LYRA</h2>

                <p>OSS Audit Platform</p>

            </div>

            <div className="sidebar-menu">

                {

                    menuItems.map((item) => (

                        <Link
                            key={item.path}
                            to={item.path}
                            className={
                                location.pathname === item.path
                                    ? "menu-item active"
                                    : "menu-item"
                            }
                        >

                            <span className="menu-icon">

                                {item.icon}

                            </span>

                            <span>

                                {item.name}

                            </span>

                        </Link>

                    ))

                }

            </div>

            <div className="sidebar-footer">

                <p>Version 1.0</p>

            </div>

        </div>

    );

}

export default Sidebar;
