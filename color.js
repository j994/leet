/* Write a higher-order React component that will add 1 to each numeric property passed to the component.

For example, if there is a component defined as */

/* const Add = ({a, b}) => <span>{a} + {b} = {a+b}</span>; */

/* const WrappedAdd = wrap(Add);

<WrappedAdd a={1} b={2} /> */

const wrap = (component) => {
  return class extends React.component {
    render() {
      const { a, b } = this.props;
      const newProps = {
        a: a + 1,
        b: b + 1,
      };
      return <component {...newProps} />;
    }
  };
};
