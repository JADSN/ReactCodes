// * Internal imports
import PropTypes from "prop-types";

const Button = ({ color, text, onClick }) => {
  // const onClick = () => {
  //   console.log("Clicked");
  // };

  return (
    <button
      type="button"
      className="btn"
      style={{ backgroundColor: color }}
      onClick={onClick}
    >
      {text}
    </button>
  );
};

// * Default props
Button.defaultProps = {
  color: "black",
  text: "Text",
};

// * PropTypes
Button.propTypes = {
  color: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired,
  onClick: PropTypes.func,
};

export default Button;
