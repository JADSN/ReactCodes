// * Internal imports
import PropTypes from "prop-types";
import { useLocation } from "react-router-dom";

// * Components
import Button from "./Button";

// const Header = (props) => {
const Header = ({ title, onAdd, showAdd }) => {
  const location = useLocation();
  return (
    <div>
      <header className="header">
        {/* <h1>{props.title}</h1> */}
        {/* <h1 style={headingSytle}>{title}</h1> */}
        <h1>{title}</h1>
        {location.pathname === "/" && (
          <Button
            color={showAdd ? "red" : "green"}
            text={showAdd ? "Close" : "Add"}
            onClick={onAdd}
          />
        )}
      </header>
    </div>
  );
};

// * CSS in JS
// const headingSytle = {
//   color: "red",
// };

// * Default props
Header.defaultProps = {
  title: "Hello Tracker",
};

// * PropTypes
Header.propTypes = {
  title: PropTypes.string.isRequired,
};

export default Header;
