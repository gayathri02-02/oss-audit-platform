import RefreshIcon from "@mui/icons-material/Refresh";
import NotificationsIcon from "@mui/icons-material/Notifications";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import SearchIcon from "@mui/icons-material/Search";

import "../assets/styles/navbar.css";

function Navbar() {

    return (

        <div className="navbar">

            <div className="navbar-left">

                <h2>Enterprise OSS Audit Platform</h2>

            </div>

            <div className="navbar-center">

                <div className="search-box">

                    <SearchIcon />

                    <input
                        type="text"
                        placeholder="Search Projects, SBOMs, Reports..."
                    />

                </div>

            </div>

            <div className="navbar-right">

                <button className="icon-button">

                    <RefreshIcon />

                </button>

                <button className="icon-button">

                    <NotificationsIcon />

                </button>

                <div className="user-profile">

                    <AccountCircleIcon />

                    <span>Administrator</span>

                </div>

            </div>

        </div>

    );

}

export default Navbar;
