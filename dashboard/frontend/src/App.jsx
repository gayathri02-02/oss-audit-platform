import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Projects from "./pages/Projects";
import SBOM from "./pages/SBOM";
import CBOM from "./pages/CBOM";
import Reports from "./pages/Reports";
import Analytics from "./pages/Analytics";

function App() {

    return (

        <BrowserRouter>

            <div
                style={{
                    display: "flex",
                    height: "100vh",
                    background: "#F5F7FA"
                }}
            >

                <Sidebar />

                <div
                    style={{
                        flex: 1,
                        display: "flex",
                        flexDirection: "column"
                    }}
                >

                    <Navbar />

                    <div
                        style={{
                            flex: 1,
                            padding: "25px",
                            overflowY: "auto"
                        }}
                    >

                        <Routes>

                            <Route
                                path="/"
                                element={<Home />}
                            />

                            <Route
                                path="/projects"
                                element={<Projects />}
                            />

                            <Route
                                path="/sboms"
                                element={<SBOM />}
                            />

                            <Route
                                path="/cboms"
                                element={<CBOM />}
                            />

                            <Route
                                path="/reports"
                                element={<Reports />}
                            />

                            <Route
                                path="/analytics"
                                element={<Analytics />}
                            />

                        </Routes>

                    </div>

                </div>

            </div>

        </BrowserRouter>

    );

}

export default App;
